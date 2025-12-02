
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: F (G4), A (Bb4), Bb (B4), D (E4)
note1 = pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25)
note3 = pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625)
note4 = pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0)
sax.notes.extend([note1, note2, note3, note4])

# Bass: walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.875),   # F3
    pretty_midi.Note(velocity=80, pitch=48, start=1.875, end=2.25),  # G3
    pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.625),  # Ab3
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0)    # Bb3
]
bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4 with 7th chords
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),   # F4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),   # A4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),   # Bb4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),   # B4
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),   # F4
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # A4
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),   # Bb4
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0)    # B4
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax motif: Repeat with variation
note5 = pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375)
note6 = pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75)
note7 = pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125)
note8 = pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5)
sax.notes.extend([note5, note6, note7, note8])

# Bass: walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),   # Bb3
    pretty_midi.Note(velocity=80, pitch=52, start=3.375, end=3.75),  # C4
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.125),  # Db4
    pretty_midi.Note(velocity=80, pitch=55, start=4.125, end=4.5)    # D4
]
bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4 with 7th chords
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),   # F4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),   # A4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),   # Bb4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),   # B4
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5),   # F4
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),   # A4
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),   # Bb4
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5)    # B4
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax motif: Finish with resolution
note9 = pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875)
note10 = pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25)
note11 = pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625)
note12 = pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0)
sax.notes.extend([note9, note10, note11, note12])

# Bass: walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=4.875),   # D4
    pretty_midi.Note(velocity=80, pitch=57, start=4.875, end=5.25),  # Eb4
    pretty_midi.Note(velocity=80, pitch=58, start=5.25, end=5.625),  # E4
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=6.0)    # F4
]
bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4 with 7th chords
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),   # F4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),   # A4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),   # Bb4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),   # B4
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0),   # F4
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),   # A4
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),   # Bb4
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0)    # B4
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.5, end=start + 1.875)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.25)
    hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875)
    hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.875, end=start + 2.25)
    hihat7 = pretty_midi.Note(velocity=100, pitch=42, start=start + 2.25, end=start + 2.625)
    hihat8 = pretty_midi.Note(velocity=100, pitch=42, start=start + 2.625, end=start + 3.0)
    drums.notes.extend([kick1, snare1, hihat1, hihat2, hihat3, hihat4, kick2, snare2, hihat5, hihat6, hihat7, hihat8])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
