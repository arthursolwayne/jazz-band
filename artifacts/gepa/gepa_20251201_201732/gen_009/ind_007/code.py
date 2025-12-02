
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kit pattern: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=1.875, end=2.0))

# Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.25),  # Eb2
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625),  # E2
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),   # G2
]

bass.notes.extend(bass_notes)

# Diane piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=3.0))

# Bar 3: Gm7 (G Bb D F)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=4.5))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=4.5))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=4.5))

# Bar 4: Cmaj7 (C E G B)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=6.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=6.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=6.0))

# Dante sax: Melody - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A4
]

sax.notes.extend(sax_notes)

# Bar 4: Return and finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # E4
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # D4
]

sax.notes.extend(sax_notes)

# Bar 3: Drums
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=4.125, end=4.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=3.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.0))

# Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=4.125, end=4.5))

# Bar 4: Drums
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=5.625, end=6.0))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=6.0, end=6.125))

# Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=5.625, end=6.0))

midi.instruments.extend([sax, bass, piano, drums])

midi.save('jazz_intro.mid')
