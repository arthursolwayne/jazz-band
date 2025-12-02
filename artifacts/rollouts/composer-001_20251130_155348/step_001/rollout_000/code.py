
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
    # Hihat on every eighth
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
# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0), # D
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.375), # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=90, pitch=61, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5), # Bb
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=90, pitch=61, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0), # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on beat 1
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875), # G
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875), # Bb
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875), # C
    # Bar 2: F7 on beat 3
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=2.8125), # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.8125), # A
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.8125), # C
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.8125), # D
    # Bar 3: Dm7 on beat 1
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375), # C
    # Bar 3: F7 on beat 3
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.3125), # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.3125), # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.3125), # C
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.3125), # D
    # Bar 4: Dm7 on beat 1
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875), # Bb
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875), # C
    # Bar 4: G7 on beat 3
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=5.8125), # G
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=5.8125), # B
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=5.8125), # D
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=5.8125), # F
]
piano.notes.extend(piano_notes)

# Sax: Motif
# Dm7: D, F, Bb, C
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875), # D
    pretty_midi.Note(velocity=110, pitch=65, start=1.6875, end=1.875), # F
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.1875), # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=3.1875, end=3.375), # F
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875), # D
    pretty_midi.Note(velocity=110, pitch=65, start=4.6875, end=4.875), # F
    pretty_midi.Note(velocity=110, pitch=60, start=4.875, end=5.0625), # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=5.0625, end=5.25), # F
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.4375), # D
    pretty_midi.Note(velocity=110, pitch=65, start=5.4375, end=5.625), # F
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=5.8125), # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=5.8125, end=6.0), # F
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
for bar in [2, 3, 4]:
    start = (bar - 1) * 1.5
    kick_start = start + 0.0
    kick_end = kick_start + 0.375
    kick2_start = start + 1.125
    kick2_end = kick2_start + 0.375
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick2_start, end=kick2_end))
    # Snare on 2 and 4
    snare_start = start + 0.75
    snare_end = snare_start + 0.125
    snare2_start = start + 1.875
    snare2_end = snare2_start + 0.125
    drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end))
    drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare2_start, end=snare2_end))
    # Hihat on every eighth
    for i in range(8):
        hihat_start = start + i * 0.375
        hihat_end = hihat_start + 0.1875
        drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
