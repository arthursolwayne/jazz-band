
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
    # Hihat on every eighth
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

# Bass line (Marcus): walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625), # Bb2 (fifth)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # F2 (root)
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # F2 (root)
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75), # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125), # Bb2 (fifth)
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # F2 (root)
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # F2 (root)
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=41, start=5.25, end=5.625), # Bb2 (fifth)
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # F2 (root)
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5 - 3.0s): Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # C4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # E4
    
    # Bar 3 (3.0 - 4.5s): Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=4.5),  # F4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # Ab4
    
    # Bar 4 (4.5 - 6.0s): C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # B4
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.5),  # B4
    pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.75),  # A4
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25),  # D5
    pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.5),  # B4
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.0),  # D5
    pretty_midi.Note(velocity=110, pitch=66, start=4.0, end=4.25),  # B4
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),  # D5
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5),  # D5
    pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.75),  # A4
    pretty_midi.Note(velocity=110, pitch=66, start=5.75, end=6.0),  # B4
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2])
    
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    drums.notes.extend([snare1, snare2])
    
    # Hihat on every eighth
    for i in range(0, 4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
