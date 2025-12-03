
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

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # A2 (fifth of D2)
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=3.0),  # G2 (root of F7)
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75), # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=46, start=3.75, end=4.125), # D3 (fifth of G2)
    pretty_midi.Note(velocity=80, pitch=44, start=4.125, end=4.5),  # C3 (root of Bb7)
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=44, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=80, pitch=46, start=4.875, end=5.25), # D3 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.625), # F3 (fifth of C3)
    pretty_midi.Note(velocity=80, pitch=47, start=5.625, end=6.0),  # E3 (root of D7)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=3.0),  # E5
]
# Bar 3: Bb7 (Bb D F A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),  # F4
    pretty_midi.Note(velocity=100, pitch=80, start=3.0, end=4.5),  # A4
])
# Bar 4: D7 (D F# A C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # F4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),  # G4 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=6.0),  # A4
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F4 - Bb4 - E4 - D4 (F - Bb - E - D)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=110, pitch=76, start=1.75, end=2.0),  # Bb4
    pretty_midi.Note(velocity=110, pitch=77, start=2.0, end=2.25),  # E4 (resting on the note before the resolution)
    pretty_midi.Note(velocity=110, pitch=72, start=2.5, end=2.75),  # F4 (returning)
    pretty_midi.Note(velocity=110, pitch=76, start=2.75, end=3.0),  # Bb4
    pretty_midi.Note(velocity=110, pitch=77, start=3.0, end=3.25),  # E4
    pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.5),  # D4 (resolution)
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),  # C4 (chromatic approach)
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.0),  # F4
    pretty_midi.Note(velocity=110, pitch=76, start=4.0, end=4.25),  # Bb4
    pretty_midi.Note(velocity=110, pitch=77, start=4.25, end=4.5),  # E4
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=5.0),  # C4
    pretty_midi.Note(velocity=110, pitch=72, start=5.0, end=5.25),  # F4
    pretty_midi.Note(velocity=110, pitch=76, start=5.25, end=5.5),  # Bb4
    pretty_midi.Note(velocity=110, pitch=77, start=5.5, end=5.75),  # E4
    pretty_midi.Note(velocity=110, pitch=71, start=5.75, end=6.0),  # D4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick3])
    
# Snare on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    drums.notes.extend([snare2, snare4])
    
# Hi-hat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + (i + 1) * 0.375)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
