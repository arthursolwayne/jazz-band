
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus on bass - walking line in F minor
# F2 (38), G2 (43), Ab2 (41), A2 (45), Bb2 (42), B2 (46), C3 (50), Db3 (48)
# Roots and fifths with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.25),  # G2
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625),  # Ab2
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),   # A2
]
bass.notes.extend(bass_notes)

# Diane on piano - open voicings, different chord each bar
# Bar 2: F7 (F, A, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # C4
]
piano.notes.extend(piano_notes)

# Dante on sax - motif: F -> Ab -> Bb -> F (hold on last note)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.875),  # F5
    pretty_midi.Note(velocity=110, pitch=70, start=1.875, end=2.25),  # Ab5
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),  # Bb5
    pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=3.0),   # F5
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus on bass - walking line in F minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=80, pitch=46, start=3.375, end=3.75),  # B2
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125),  # C3
    pretty_midi.Note(velocity=80, pitch=48, start=4.125, end=4.5),   # Db3
]
bass.notes.extend(bass_notes)

# Diane on piano - open voicings, different chord each bar
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F5
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Ab4
]
piano.notes.extend(piano_notes)

# Dante on sax - motif: F -> Ab -> Bb -> F (hold on last note)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.375),  # F5
    pretty_midi.Note(velocity=110, pitch=70, start=3.375, end=3.75),  # Ab5
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125),  # Bb5
    pretty_midi.Note(velocity=110, pitch=72, start=4.125, end=4.5),   # F5
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus on bass - walking line in F minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25),  # G2
    pretty_midi.Note(velocity=80, pitch=41, start=5.25, end=5.625),  # Ab2
    pretty_midi.Note(velocity=80, pitch=45, start=5.625, end=6.0),   # A2
]
bass.notes.extend(bass_notes)

# Diane on piano - open voicings, different chord each bar
# Bar 4: F7 (F, A, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # C4
]
piano.notes.extend(piano_notes)

# Dante on sax - motif: F -> Ab -> Bb -> F (hold on last note)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.875),  # F5
    pretty_midi.Note(velocity=110, pitch=70, start=4.875, end=5.25),  # Ab5
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625),  # Bb5
    pretty_midi.Note(velocity=110, pitch=72, start=5.625, end=6.0),   # F5
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=42, start=7.125, end=7.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.save('dante_russo.mid')
