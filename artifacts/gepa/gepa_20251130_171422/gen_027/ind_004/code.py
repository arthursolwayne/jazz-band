
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Melody starts here
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=56, start=1.5, end=1.875),  # Fm7 (F, Ab, Bb, D)
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.25), # D (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=56, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=58, start=2.625, end=3.0),  # G
]
sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=46, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=45, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=100, pitch=48, start=2.625, end=3.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 (F7 chord)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # D
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # D (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=56, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=58, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=56, start=4.125, end=4.5),  # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=45, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=48, start=4.125, end=4.5),  # G
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 (F7 chord)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # D
]
piano.notes.extend(piano_notes)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # D (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=56, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=58, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=56, start=5.625, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=48, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=45, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=100, pitch=48, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 (F7 chord)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=57, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro_in_Fm.mid")
