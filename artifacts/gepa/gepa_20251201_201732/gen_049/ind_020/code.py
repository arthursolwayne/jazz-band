
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
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),  # kick
    pretty_midi.Note(velocity=80, pitch=38, start=0.375, end=0.75),  # snare
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=1.5),     # hihat
    pretty_midi.Note(velocity=80, pitch=36, start=0.75, end=1.125),  # kick
    pretty_midi.Note(velocity=80, pitch=38, start=1.125, end=1.5),   # snare
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Root and fifth with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.75),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=42, start=1.75, end=2.0),  # C#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.25),  # A2 (fifth)
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.5),  # A2
    pretty_midi.Note(velocity=80, pitch=45, start=2.5, end=2.75),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.75, end=3.0),  # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicing, Dmaj7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.75),  # D5
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # C#5
    # Bar 2, beat 2: Gm7
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=2.0, end=2.25),  # B4
    pretty_midi.Note(velocity=90, pitch=77, start=2.0, end=2.25),  # D6
    pretty_midi.Note(velocity=90, pitch=76, start=2.0, end=2.25),  # C#6
    # Bar 2, beat 3: C#7
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=2.75),  # C#5
    pretty_midi.Note(velocity=90, pitch=77, start=2.5, end=2.75),  # E6
    pretty_midi.Note(velocity=90, pitch=82, start=2.5, end=2.75),  # G6
    pretty_midi.Note(velocity=90, pitch=81, start=2.5, end=2.75),  # F#6
    # Bar 2, beat 4: A7
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.25),  # A5
    pretty_midi.Note(velocity=90, pitch=82, start=3.0, end=3.25),  # C#6
    pretty_midi.Note(velocity=90, pitch=87, start=3.0, end=3.25),  # E6
    pretty_midi.Note(velocity=90, pitch=86, start=3.0, end=3.25),  # D6
]
piano.notes.extend(piano_notes)

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=1.5, end=1.875),  # kick
    pretty_midi.Note(velocity=80, pitch=38, start=1.875, end=2.25),  # snare
    pretty_midi.Note(velocity=60, pitch=42, start=1.5, end=3.0),     # hihat
    pretty_midi.Note(velocity=80, pitch=36, start=2.25, end=2.625),  # kick
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),   # snare
]
drums.notes.extend(drum_notes)

# Sax: Motif (1.5 - 2.0s), leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # D4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Root and fifth with chromatic approach (Dm7)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.25),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=44, start=3.25, end=3.5),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=47, start=3.5, end=3.75),  # A2 (fifth)
    pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=4.0),  # A2
    pretty_midi.Note(velocity=80, pitch=45, start=4.0, end=4.25),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=4.25, end=4.5),  # D2
]
bass.notes.extend(bass_notes)

# Piano: Dm7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # C#5
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.25),  # D5
    # Bar 3, beat 2: F7
    pretty_midi.Note(velocity=90, pitch=65, start=3.5, end=3.75),  # F4
    pretty_midi.Note(velocity=90, pitch=70, start=3.5, end=3.75),  # C5
    pretty_midi.Note(velocity=90, pitch=75, start=3.5, end=3.75),  # F6
    pretty_midi.Note(velocity=90, pitch=74, start=3.5, end=3.75),  # E6
    # Bar 3, beat 3: B7
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.25),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=4.0, end=4.25),  # E6
    pretty_midi.Note(velocity=90, pitch=79, start=4.0, end=4.25),  # G6
    pretty_midi.Note(velocity=90, pitch=78, start=4.0, end=4.25),  # F#6
    # Bar 3, beat 4: C#7
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.75),  # C#5
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.75),  # E6
    pretty_midi.Note(velocity=90, pitch=82, start=4.5, end=4.75),  # G6
    pretty_midi.Note(velocity=90, pitch=81, start=4.5, end=4.75),  # F#6
]
piano.notes.extend(piano_notes)

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=3.0, end=3.375),  # kick
    pretty_midi.Note(velocity=80, pitch=38, start=3.375, end=3.75),  # snare
    pretty_midi.Note(velocity=60, pitch=42, start=3.0, end=4.5),     # hihat
    pretty_midi.Note(velocity=80, pitch=36, start=3.75, end=4.125),  # kick
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),   # snare
]
drums.notes.extend(drum_notes)

# Sax: Continue motif (3.0 - 4.0s), finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Root and fifth with chromatic approach (Dmaj7)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.75),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=5.0),  # C#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=47, start=5.0, end=5.25),  # A2 (fifth)
    pretty_midi.Note(velocity=80, pitch=47, start=5.25, end=5.5),  # A2
    pretty_midi.Note(velocity=80, pitch=45, start=5.5, end=5.75),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=5.75, end=6.0),  # D2
]
bass.notes.extend(bass_notes)

# Piano: Dmaj7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.75),  # D5
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # C#5
    # Bar 4, beat 2: Gmaj7
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.25),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=5.0, end=5.25),  # B4
    pretty_midi.Note(velocity=90, pitch=77, start=5.0, end=5.25),  # D6
    pretty_midi.Note(velocity=90, pitch=76, start=5.0, end=5.25),  # C#6
    # Bar 4, beat 3: C#7
    pretty_midi.Note(velocity=90, pitch=72, start=5.5, end=5.75),  # C#5
    pretty_midi.Note(velocity=90, pitch=77, start=5.5, end=5.75),  # E6
    pretty_midi.Note(velocity=90, pitch=82, start=5.5, end=5.75),  # G6
    pretty_midi.Note(velocity=90, pitch=81, start=5.5, end=5.75),  # F#6
    # Bar 4, beat 4: A7
    pretty_midi.Note(velocity=90, pitch=77, start=6.0, end=6.25),  # A5
    pretty_midi.Note(velocity=90, pitch=82, start=6.0, end=6.25),  # C#6
    pretty_midi.Note(velocity=90, pitch=87, start=6.0, end=6.25),  # E6
    pretty_midi.Note(velocity=90, pitch=86, start=6.0, end=6.25),  # D6
]
piano.notes.extend(piano_notes)

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=4.5, end=4.875),  # kick
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25),  # snare
    pretty_midi.Note(velocity=60, pitch=42, start=4.5, end=6.0),     # hihat
    pretty_midi.Note(velocity=80, pitch=36, start=5.25, end=5.625),  # kick
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),   # snare
]
drums.notes.extend(drum_notes)

# Sax: Rest
# No notes needed here

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
