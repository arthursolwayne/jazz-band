
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=58, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),  # C
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=54, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=90, pitch=56, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=58, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=59, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=90, pitch=55, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = []
bar_start = 1.5
for bar in range(2, 5):
    # Bar 2 (1.5 - 3.0)
    if bar == 2:
        # Dm7 on beat 2
        for pitch in [62, 67, 71, 75]:  # Dm7 (D, F, A, C)
            piano_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=bar_start + 0.75, end=bar_start + 1.125))
        # Dm7 on beat 4
        for pitch in [62, 67, 71, 75]:
            piano_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=bar_start + 1.875, end=bar_start + 2.25))
    # Bar 3 (3.0 - 4.5)
    elif bar == 3:
        # G7 on beat 2
        for pitch in [67, 71, 74, 78]:  # G7 (G, B, D, F)
            piano_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=bar_start + 0.75, end=bar_start + 1.125))
        # G7 on beat 4
        for pitch in [67, 71, 74, 78]:
            piano_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=bar_start + 1.875, end=bar_start + 2.25))
    # Bar 4 (4.5 - 6.0)
    elif bar == 4:
        # Dm7 on beat 2
        for pitch in [62, 67, 71, 75]:
            piano_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=bar_start + 0.75, end=bar_start + 1.125))
        # Dm7 on beat 4
        for pitch in [62, 67, 71, 75]:
            piano_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=bar_start + 1.875, end=bar_start + 2.25))
    bar_start += 1.5

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # E
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.1875, end=3.375), # E
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875), # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0625), # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.0625, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.4375), # E
    pretty_midi.Note(velocity=100, pitch=67, start=5.4375, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.8125), # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.8125, end=6.0),  # E
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    bar_start = 1.5 * (bar - 1)
    kick_start = bar_start + 0.0
    kick_end = bar_start + 0.375
    kick2_start = bar_start + 1.125
    kick2_end = bar_start + 1.5
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick2_start, end=kick2_end))

    # Snare on 2 and 4
    snare_start = bar_start + 0.75
    snare_end = bar_start + 0.875
    snare2_start = bar_start + 1.875
    snare2_end = bar_start + 2.0
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end))
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare2_start, end=snare2_end))

    # Hi-hat on every eighth
    for i in range(8):
        start = bar_start + (i * 0.1875)
        end = start + 0.1875
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dm_intro.mid")
