
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # F#2 (chromatic approach)
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125), # G2
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),  # F#2 (chromatic approach)
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),  # F#2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # E5
]
# Bar 3: Bm7b5 (B, D, F#, A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # A4
])
# Bar 4: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # F4
])
piano.notes.extend(piano_notes)

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F4, A4, G4, F4 (hanging on G4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),   # A4
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),  # F4
    
    # Repeat motif with slight variation, starting on the & of 3
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.0),  # F4
    
    # Final statement, full motif
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=5.0),   # A4
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),  # G4
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5),  # F4
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
