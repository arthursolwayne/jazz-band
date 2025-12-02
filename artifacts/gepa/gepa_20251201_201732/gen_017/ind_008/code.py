
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bar 2: Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Eb2 on 2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2 on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # F2 on 4
]
bass.notes.extend(bass_notes)

# Bar 2: Piano (Fmaj7, A7, C7, Dm7)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A (7th)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C (root)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # E (7th)
    
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A (root)
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # C (3rd)
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),  # E (5th)
    pretty_midi.Note(velocity=100, pitch=81, start=1.875, end=2.25),  # G# (7th)
    
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # C (root)
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # E (3rd)
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),  # G (5th)
    pretty_midi.Note(velocity=100, pitch=80, start=2.25, end=2.625),  # Bb (7th)
    
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # D (root)
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # F (3rd)
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),   # A (5th)
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),   # C (7th)
]
piano.notes.extend(piano_notes)

# Bar 2: Sax melody (motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # G (F7)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # E (Dm7)
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # G (F7)
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),   # E (Dm7)
]
sax.notes.extend(sax_notes)

# Bar 3: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 3: Bass line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # F2 on 1
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.75), # G2 on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # F2 on 3
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),  # Eb2 on 4
]
bass.notes.extend(bass_notes)

# Bar 3: Piano (Fmaj7, D7, C7, Gm7)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F (root)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A (7th)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # C (root)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # E (7th)
    
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # D (root)
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # F (3rd)
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # A (5th)
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),  # C (7th)
    
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # C (root)
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # E (3rd)
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125),  # G (5th)
    pretty_midi.Note(velocity=100, pitch=80, start=3.75, end=4.125),  # Bb (7th)
    
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),   # C (root)
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),   # E (3rd)
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),   # G (5th)
    pretty_midi.Note(velocity=100, pitch=77, start=4.125, end=4.5),   # Bb (7th)
]
piano.notes.extend(piano_notes)

# Bar 3: Sax melody (continuation)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # E (F7)
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # G (D7)
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # E (C7)
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),   # G (Gm7)
]
sax.notes.extend(sax_notes)

# Bar 4: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Bass line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.875),  # Eb2 on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # F2 on 2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # G2 on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # F2 on 4
]
bass.notes.extend(bass_notes)

# Bar 4: Piano (Fmaj7, A7, C7, Dm7)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A (7th)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C (root)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # E (7th)
    
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # A (root)
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # C (3rd)
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),  # E (5th)
    pretty_midi.Note(velocity=100, pitch=81, start=4.875, end=5.25),  # G# (7th)
    
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # C (root)
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),  # E (3rd)
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625),  # G (5th)
    pretty_midi.Note(velocity=100, pitch=80, start=5.25, end=5.625),  # Bb (7th)
    
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # D (root)
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # F (3rd)
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),   # A (5th)
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),   # C (7th)
]
piano.notes.extend(piano_notes)

# Bar 4: Sax melody (finish the motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # G (F7)
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # E (Dm7)
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # G (F7)
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),   # E (Dm7)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('wayne_intro.mid')
