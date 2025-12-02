
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=48, start=2.625, end=3.0),  # G#
    pretty_midi.Note(velocity=100, pitch=49, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75), # A#
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=100, pitch=52, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=100, pitch=54, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=5.625), # D#
    pretty_midi.Note(velocity=100, pitch=56, start=5.625, end=6.0),  # E
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875), # E
    # Bar 3: B7 (B, D#, F#, A)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375), # B
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375), # D#
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.375), # F#
    pretty_midi.Note(velocity=100, pitch=83, start=3.0, end=3.375), # A
    # Bar 4: E7 (E, G#, B, D)
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875), # E
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=4.875), # G#
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=4.875), # B
    pretty_midi.Note(velocity=100, pitch=86, start=4.5, end=4.875), # D
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=68, start=1.75, end=2.0),   # B
    pretty_midi.Note(velocity=110, pitch=70, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=110, pitch=68, start=2.25, end=2.5),  # B
    pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=68, start=4.25, end=4.5),  # B
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick_start = bar_start + 0.0
    kick_end = kick_start + 0.375
    snare_start = bar_start + 0.375
    snare_end = snare_start + 0.375
    kick2_start = bar_start + 0.75
    kick2_end = kick2_start + 0.375
    snare2_start = bar_start + 1.125
    snare2_end = snare2_start + 0.375
    hihat_start = bar_start
    hihat_end = bar_start + 1.5
    for note in [
        pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end),
        pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end),
        pretty_midi.Note(velocity=100, pitch=36, start=kick2_start, end=kick2_end),
        pretty_midi.Note(velocity=100, pitch=38, start=snare2_start, end=snare2_end),
        pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_end),
    ]:
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
