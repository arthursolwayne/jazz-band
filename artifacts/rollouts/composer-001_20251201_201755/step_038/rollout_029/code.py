
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

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # Fm root (D2)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25), # Fm 3rd (F2)
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625), # chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # Fm root (D2)
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # Fm 5th (G2)
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75), # Fm 3rd (F2)
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125), # chromatic approach
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # Fm 5th (G2)
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # Fm root (D2)
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25), # Fm 3rd (F2)
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625), # chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # Fm root (D2)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, D, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # Ab (Ab4)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # D (D5)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # C (C5)
]

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Bb (Bb4)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # D (D5)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # F (F5)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # Ab (Ab4)
])

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C (C4)
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),  # Eb (Eb4)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G (G4)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # Bb (Bb4)
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Fm (F, Ab, D, C) with a descending line
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.6875),  # F (F4)
    pretty_midi.Note(velocity=110, pitch=60, start=1.6875, end=1.875), # Ab (Ab4)
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0625), # D (D5)
    pretty_midi.Note(velocity=110, pitch=67, start=2.0625, end=2.25), # C (C5)
    
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=2.8125),  # F (F4)
    pretty_midi.Note(velocity=110, pitch=60, start=2.8125, end=3.0),    # Ab (Ab4)
    
    # Come back and finish it
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.3125), # D (D5)
    pretty_midi.Note(velocity=110, pitch=67, start=4.3125, end=4.5),   # C (C5)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    kick_start = start
    kick_end = kick_start + 0.375
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)
    drums.notes.append(kick_note)
    
    kick_start = start + 1.125
    kick_end = kick_start + 0.375
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)
    drums.notes.append(kick_note)
    
    # Snare on 2 and 4
    snare_start = start + 0.75
    snare_end = snare_start + 0.125
    snare_note = pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end)
    drums.notes.append(snare_note)
    
    snare_start = start + 1.875
    snare_end = snare_start + 0.125
    snare_note = pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end)
    drums.notes.append(snare_note)
    
    # Hihat on every eighth
    for eighth in range(0, 8):
        hihat_start = start + (eighth * 0.375)
        hihat_end = hihat_start + 0.1875
        hihat_note = pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_end)
        drums.notes.append(hihat_note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
