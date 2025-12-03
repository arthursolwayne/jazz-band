
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus - Walking bass line in F (D2-G2, MIDI 38-43)
bass_notes = [
    # F (D2) - root
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    # Bb (F2) - fifth with chromatic approach
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),
    # C (G2) - root
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),
    # D (A2) - fifth with chromatic approach
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Diane - Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25),  # E
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # Ab
])
piano.notes.extend(piano_notes)

# Dante - Motif: F - Bb - C - D (MIDI 65-68-72-72)
# Start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=3.0),  # D
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus - Walking bass line (F to Bb)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=45, start=3.75, end=4.125),  # Bb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),  # F
]
bass.notes.extend(bass_notes)

# Diane - Open voicings, different chord each bar, resolve on the last
# Bar 3: C7 (C, E, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # Bb
]
# Bar 4: Fmaj7 (F, A, C, E)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.5),  # E
])
piano.notes.extend(piano_notes)

# Dante - Return the motif, finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=110, pitch=72, start=4.125, end=4.5),  # D
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus - Walking bass line (F to Bb)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=45, start=5.25, end=5.625),  # Bb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Diane - Open voicings, different chord each bar, resolve on the last
# Bar 4: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.25),  # E
]
# Bar 4: Rest on the last beat
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=6.0),  # E
])
piano.notes.extend(piano_notes)

# Dante - End the motif on F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
