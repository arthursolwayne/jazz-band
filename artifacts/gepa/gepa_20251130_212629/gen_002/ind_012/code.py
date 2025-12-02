
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75), # D (beat 1)
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=2.0), # Eb (beat 2)
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25), # F (beat 3)
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5), # E (beat 4)
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75), # D (beat 1)
    pretty_midi.Note(velocity=100, pitch=63, start=2.75, end=3.0), # Eb (beat 2)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25), # F (beat 3)
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5), # E (beat 4)
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75), # D (beat 1)
    pretty_midi.Note(velocity=100, pitch=63, start=3.75, end=4.0), # Eb (beat 2)
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25), # F (beat 3)
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5), # E (beat 4)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75), # D (beat 1)
    pretty_midi.Note(velocity=100, pitch=63, start=4.75, end=5.0), # Eb (beat 2)
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25), # F (beat 3)
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5), # E (beat 4)
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    # Bar 2: D7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.75), # D
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.75), # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75), # C
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.5), # D
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5), # F
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.5), # A
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.5), # C
    # Bar 3: D7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=70, start=2.75, end=3.0), # D
    pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=3.0), # F
    pretty_midi.Note(velocity=100, pitch=74, start=2.75, end=3.0), # A
    pretty_midi.Note(velocity=100, pitch=76, start=2.75, end=3.0), # C
    pretty_midi.Note(velocity=100, pitch=70, start=3.5, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.5, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=3.75), # C
    # Bar 4: D7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=70, start=4.25, end=4.5), # D
    pretty_midi.Note(velocity=100, pitch=72, start=4.25, end=4.5), # F
    pretty_midi.Note(velocity=100, pitch=74, start=4.25, end=4.5), # A
    pretty_midi.Note(velocity=100, pitch=76, start=4.25, end=4.5), # C
    pretty_midi.Note(velocity=100, pitch=70, start=5.0, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=74, start=5.0, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=76, start=5.0, end=5.25), # C
]
piano.notes.extend(piano_notes)

# Sax (Dante)
sax_notes = [
    # Bar 2: Melody starts
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0), # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25), # D
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5), # Bb
    # Bar 3: Repeat and leave it hanging
    pretty_midi.Note(velocity=110, pitch=65, start=2.75, end=3.0), # F
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25), # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5), # D
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75), # Bb
    # Bar 4: Return and resolve
    pretty_midi.Note(velocity=110, pitch=65, start=4.0, end=4.25), # F
    pretty_midi.Note(velocity=110, pitch=69, start=4.25, end=4.5), # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75), # D
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=5.0), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25), # D
]
sax.notes.extend(sax_notes)

# Drum fills in bars 2-4
drum_notes_2 = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.375), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.1875), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.375, end=2.75), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.375, end=2.5625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.75, end=3.125), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.75, end=2.9375), # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.875), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.5, end=3.6875), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.875, end=4.25), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.875, end=4.0625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.25, end=4.625), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.25, end=4.4375), # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.375), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.0, end=5.1875), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.375, end=5.75), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.375, end=5.5625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.75, end=6.0), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.75, end=5.9375), # Hihat on 4
]
drums.notes.extend(drum_notes_2)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
