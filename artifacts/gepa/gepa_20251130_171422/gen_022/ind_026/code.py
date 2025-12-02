
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Build tension with space and subtle dynamics
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=85, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=95, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=55, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=55, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=55, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=55, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Saxophone motif: concise, emotional, and memorable
sax_notes = [
    # Bar 2: start the motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75), # D
    pretty_midi.Note(velocity=95, pitch=66, start=1.75, end=2.0), # F
    # Bar 3: leave it hanging, then return
    pretty_midi.Note(velocity=105, pitch=67, start=2.5, end=2.75), # F#
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0), # D
    # Bar 4: complete the motif with a twist
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75), # Eb
    pretty_midi.Note(velocity=105, pitch=66, start=3.75, end=4.0), # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25), # D
    pretty_midi.Note(velocity=95, pitch=60, start=4.25, end=4.5), # C
]
sax.notes.extend(sax_notes)

# Bass line: active, melodic, chromatic
bass_notes = [
    # Bar 2: F, Eb, D, C
    pretty_midi.Note(velocity=70, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=65, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=70, pitch=60, start=2.0, end=2.25),
    pretty_midi.Note(velocity=65, pitch=59, start=2.25, end=2.5),
    # Bar 3: Bb, A, G, F
    pretty_midi.Note(velocity=70, pitch=57, start=2.5, end=2.75),
    pretty_midi.Note(velocity=65, pitch=55, start=2.75, end=3.0),
    pretty_midi.Note(velocity=70, pitch=53, start=3.0, end=3.25),
    pretty_midi.Note(velocity=65, pitch=64, start=3.25, end=3.5),
    # Bar 4: C, Bb, A, G
    pretty_midi.Note(velocity=70, pitch=60, start=3.5, end=3.75),
    pretty_midi.Note(velocity=65, pitch=57, start=3.75, end=4.0),
    pretty_midi.Note(velocity=70, pitch=55, start=4.0, end=4.25),
    pretty_midi.Note(velocity=65, pitch=53, start=4.25, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: comp with emotion, 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=2.0), # D
    pretty_midi.Note(velocity=75, pitch=67, start=1.75, end=2.0), # F#
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0), # Eb
    pretty_midi.Note(velocity=75, pitch=69, start=1.75, end=2.0), # G
    # Bar 3: Dm7 on 2
    pretty_midi.Note(velocity=80, pitch=62, start=2.75, end=3.0), # D
    pretty_midi.Note(velocity=75, pitch=67, start=2.75, end=3.0), # F#
    pretty_midi.Note(velocity=80, pitch=64, start=2.75, end=3.0), # Eb
    pretty_midi.Note(velocity=75, pitch=69, start=2.75, end=3.0), # G
    # Bar 4: Dm7 on 4
    pretty_midi.Note(velocity=80, pitch=62, start=4.25, end=4.5), # D
    pretty_midi.Note(velocity=75, pitch=67, start=4.25, end=4.5), # F#
    pretty_midi.Note(velocity=80, pitch=64, start=4.25, end=4.5), # Eb
    pretty_midi.Note(velocity=75, pitch=69, start=4.25, end=4.5), # G
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
