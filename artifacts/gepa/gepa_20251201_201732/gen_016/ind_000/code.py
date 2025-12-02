
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

# Drums: Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875)    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Bar 2 - Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # G2 (Fm root 5)
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25), # F2 (Fm root)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=80, pitch=44, start=2.625, end=3.0),  # Ab2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Bar 2 - Open voicing, Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # Eb4
    pretty_midi.Note(velocity=90, pitch=73, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=90, pitch=78, start=1.5, end=1.875),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Bar 2 - Start motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # D4 (Fm 9)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # E4 (Fm 11)
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # C4 (Fm root)
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),  # D4 (Fm 9)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375)    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Bar 3 - Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),  # D2 (Fm 3)
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75), # G2 (Fm 5)
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125), # F2 (Fm root)
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5),  # Eb2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Bar 3 - Open voicing, Bbm7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # Ab4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: Bar 3 - Continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb3 (Fm 7)
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # D4 (Fm 9)
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # Bb3
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # C4 (Fm root)
]
sax.notes.extend(sax_notes)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875)    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Bar 4 - Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=4.5, end=4.875),  # D2 (Fm 3)
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25), # G2 (Fm 5)
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625), # F2 (Fm root)
    pretty_midi.Note(velocity=80, pitch=41, start=5.625, end=6.0),  # Eb2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Bar 4 - Open voicing, Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=90, pitch=73, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # Ab4
    pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=4.875),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Bar 4 - End motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # D4 (Fm 9)
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # E4 (Fm 11)
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # C4 (Fm root)
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0),  # D4 (Fm 9)
]
sax.notes.extend(sax_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375)    # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
