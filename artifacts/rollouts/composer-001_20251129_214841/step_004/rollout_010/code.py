
import pretty_midi

midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0, tempo=120.0)]

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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    # C -> Eb -> D -> F
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),
    # Bar 3 (3.0 - 4.5s)
    # G -> Bb -> A -> B
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=70, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),
    # Bar 4 (4.5 - 6.0s)
    # C -> Eb -> D -> F
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=63, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    # C7 on beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),
    # C7 on beat 4
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),
    # Bar 3 (3.0 - 4.5s)
    # F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.0),
    # F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75),
    # Bar 4 (4.5 - 6.0s)
    # C7 on beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75),
    # C7 on beat 4
    pretty_midi.Note(velocity=100, pitch=60, start=6.0, end=6.25),
    pretty_midi.Note(velocity=100, pitch=64, start=6.0, end=6.25),
    pretty_midi.Note(velocity=100, pitch=67, start=6.0, end=6.25),
    pretty_midi.Note(velocity=100, pitch=71, start=6.0, end=6.25)
]
piano.notes.extend(piano_notes)

# Sax: your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    # Motif: C -> Eb -> D -> F (start on beat 1)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),
    # Bar 3 (3.0 - 4.5s)
    # Motif again, but with a twist: C -> F -> D -> B
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),
    # Bar 4 (4.5 - 6.0s)
    # Finish the motif: C -> Eb -> D -> F (final resolution)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=63, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),
    # Let it hang on the last note
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat on every eighth
    for i in range(4):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
