
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25), # C (fifth)
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625), # Bb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # F (root)
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # F (root)
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75), # C (fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125), # A (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # F (root)
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25), # C (fifth)
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625), # G (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0)   # F (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C E♭)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F (C4)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # A (E4)
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=3.0),  # C (G4)
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=3.0),  # E♭ (F4)
]

# Bar 3: B♭7 (B♭ D F A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # B♭ (E3)
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # D (F3)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),  # F (G3)
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=4.5),  # A (A3)
])

# Bar 4: C7 (C E G B♭)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C (C3)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # E (E3)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G (G3)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # B♭ (B♭3)
])

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (G4) - A (B4) - B♭ (C5) - F (G4)
# Start at 1.5s, leave it hanging at 2.0s, return at 3.0s to finish
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),  # F (G4)
    pretty_midi.Note(velocity=110, pitch=76, start=1.875, end=2.25),  # A (B4)
    pretty_midi.Note(velocity=110, pitch=77, start=2.25, end=2.625),  # B♭ (C5)
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375),  # F (G4)
    pretty_midi.Note(velocity=110, pitch=76, start=3.375, end=3.75),  # A (B4)
    pretty_midi.Note(velocity=110, pitch=77, start=3.75, end=4.125),  # B♭ (C5)
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),  # F (G4)
    pretty_midi.Note(velocity=110, pitch=76, start=4.5, end=4.875),  # A (B4)
    pretty_midi.Note(velocity=110, pitch=77, start=4.875, end=5.25),  # B♭ (C5)
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.625),  # F (G4)
    pretty_midi.Note(velocity=110, pitch=76, start=5.625, end=6.0)   # A (B4)
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4 (1.5 - 6.0s)
# Kick on 1 and 3
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    kick_start = start
    kick_end = kick_start + 0.375
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)
    drums.notes.append(kick)
    kick_start = start + 1.125
    kick_end = kick_start + 0.375
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)
    drums.notes.append(kick)

# Snare on 2 and 4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    snare_start = start + 0.75
    snare_end = snare_start + 0.125
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end)
    drums.notes.append(snare)
    snare_start = start + 1.875
    snare_end = snare_start + 0.125
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end)
    drums.notes.append(snare)

# Hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    for i in range(8):
        hihat_start = start + i * 0.1875
        hihat_end = hihat_start + 0.1875
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_end)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
