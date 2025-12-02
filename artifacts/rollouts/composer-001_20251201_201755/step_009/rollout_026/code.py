
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # F2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),  # Ab2 (chromatic approach)
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75), # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.125), # C3
    pretty_midi.Note(velocity=100, pitch=46, start=4.125, end=4.5),  # Bb2 (chromatic approach)
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25), # D3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625), # E3
    pretty_midi.Note(velocity=100, pitch=51, start=5.625, end=6.0),  # D3 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # C5
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # Eb4
]

# Bar 3: Bb7 (Bb D F Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5),  # Ab4
])

# Bar 4: C7 (C E G B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.0),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.0),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # B4
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F4 - G4 - Bb4 (melody in F), then let it hang on Bb4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),   # G4
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # A4 (non-diatonic)
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # Bb4
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # Bb4 (hang)
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=3.0),  # Bb4 (hang)
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # Bb4 (hang)
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),  # Bb4 (hang)
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),  # Bb4 (hang)
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # Bb4 (hang)
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25),  # Bb4 (hang)
    pretty_midi.Note(velocity=110, pitch=62, start=4.25, end=4.5),  # Bb4 (hang)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # Bb4 (hang)
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0),  # Bb4 (hang)
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),  # Bb4 (hang)
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # Bb4 (hang)
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),  # Bb4 (hang)
    pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=6.0),  # Bb4 (hang)
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4 (1.5 - 6.0s)
# Kick on 1 and 3
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick3])

# Snare on 2 and 4
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    drums.notes.extend([snare2, snare4])

# Hi-hat on every eighth
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
