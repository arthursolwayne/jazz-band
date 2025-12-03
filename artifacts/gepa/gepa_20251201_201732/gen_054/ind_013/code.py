
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.0, end=0.375),  # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),   # hihat on 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm (F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.625), # D2
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),  # C2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, Fm7, Bbm7, Eb7, Am7
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),   # F4
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=3.0),   # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),   # C5
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=3.0),   # D5
    # Bar 3: Bbm7 (Bb, Db, F, G)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),   # Bb4
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=4.5),   # Db4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),   # F5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),   # G5
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=6.0),   # Eb4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),   # G4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),   # Bb4
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=6.0),   # D5
    # Bar 2: Comp on 2 and 4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625), # F4
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.625), # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # C5
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625), # D5
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.875),  # Db4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F5
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Motif: F, Ab, D, C (Fm chord) but rhythmically displaced
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=61, start=1.875, end=2.25), # Ab4
    pretty_midi.Note(velocity=110, pitch=68, start=2.25, end=2.625), # D5
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),  # C5
    # Second pass, same motif
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=110, pitch=61, start=4.875, end=5.25), # Ab4
    pretty_midi.Note(velocity=110, pitch=68, start=5.25, end=5.625), # D5
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0),  # C5
]
sax.notes.extend(sax_notes)

# Bar 1: Drums only
# Bar 2-4: Full quartet

# Bar 2: Drums continue
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.875, end=2.25), # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # snare on 4
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75), # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # snare on 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25), # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # snare on 4
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # kick on 1
    # Hi-hats
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25), # hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # hihat on 1
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
