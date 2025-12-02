
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),

    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),    # F
    pretty_midi.Note(velocity=100, pitch=44, start=1.875, end=2.25),   # G
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),   # E
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),    # F

    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375),    # A
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.75),   # G
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),   # F
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),    # E

    pretty_midi.Note(velocity=100, pitch=41, start=4.5, end=4.875),    # D
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.25),   # F
    pretty_midi.Note(velocity=100, pitch=44, start=5.25, end=5.625),   # G
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)     # E
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords on 2 and 4
# F7 on beat 2 of bar 2, A7 on beat 2 of bar 3, D7 on beat 2 of bar 4
piano_notes = [
    # Bar 2, beat 2: F7 (F A C E)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=73, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625),  # D

    # Bar 3, beat 2: A7 (A C# E G)
    pretty_midi.Note(velocity=100, pitch=81, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=84, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=100, pitch=86, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=88, start=3.75, end=4.125),  # F#

    # Bar 4, beat 2: D7 (D F# A C)
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.625),  # B
]
piano.notes.extend(piano_notes)

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F, Bb, Ab, F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875), # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0625), # Ab
    pretty_midi.Note(velocity=110, pitch=71, start=2.0625, end=2.25),  # F

    # Repeat the motif, slightly higher
    pretty_midi.Note(velocity=110, pitch=76, start=2.625, end=2.8125),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=2.8125, end=3.0),   # Bb
    pretty_midi.Note(velocity=110, pitch=74, start=3.0, end=3.1875),   # Ab
    pretty_midi.Note(velocity=110, pitch=76, start=3.1875, end=3.375), # F

    # Final variation
    pretty_midi.Note(velocity=110, pitch=81, start=3.75, end=3.9375),  # F
    pretty_midi.Note(velocity=110, pitch=77, start=3.9375, end=4.125), # Bb
    pretty_midi.Note(velocity=110, pitch=79, start=4.125, end=4.3125), # Ab
    pretty_midi.Note(velocity=110, pitch=81, start=4.3125, end=4.5)    # F
]
sax.notes.extend(sax_notes)

# Drums continue with the same pattern for bars 2-4
for bar in range(2, 4):
    for note in drum_notes:
        note.start += 1.5 * bar
        note.end += 1.5 * bar
        note.start += 1.5 * (bar - 2)
        note.end += 1.5 * (bar - 2)
    drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
