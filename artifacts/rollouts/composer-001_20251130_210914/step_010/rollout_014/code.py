
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D (root)
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=2.0),  # Eb (chromatic)
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # C (b3)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D (root)
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),  # E (5)
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # D (root)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),  # C (b3)
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # D (root)
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # E (5)
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D (root)
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),  # E (5)
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # D (root)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # C (b3)
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # D (root)
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),  # E (5)
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D (root)
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),  # C (b3)
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # D (root)
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # D7 (D)
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.75),  # A (7)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F# (3)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75),  # C# (5)
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # D7 (D)
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.5),  # A (7)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # F# (3)
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.5),  # C# (5)
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # D7 (D)
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75),  # A (7)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # F# (3)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75),  # C# (5)
]
piano.notes.extend(piano_notes)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # E (melody)
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # G (melody)
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.25),  # D (melody)
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),  # E (melody)
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # C (resolve)
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5),  # D (resolve)
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.75),  # E (resolve)
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0),  # G (resolve)
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.75),  # D (finish)
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),  # E (finish)
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),  # G (finish)
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.5),  # D (finish)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.375),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=2.875),  # Snare on 4
]
# Bar 3
drum_notes += [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.0, end=4.375),  # Snare on 4
]
# Bar 4
drum_notes += [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.375),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.5, end=5.875),  # Snare on 4
]
# Hi-hats
for start in [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]:
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
