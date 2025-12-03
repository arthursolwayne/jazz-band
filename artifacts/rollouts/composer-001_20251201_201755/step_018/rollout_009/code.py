
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick_time = start + 0.0
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)
    kick_time = start + 0.75
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare_time = start + 0.375
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)
    snare_time = start + 1.125
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat_time = start + i * 0.375
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: Dm (D2, F2, A2)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.5 + 0.375),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=1.875 + 0.375),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.25 + 0.375),  # A2
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=2.625 + 0.375),  # G2 (chromatic approach)
]

# Bar 3: Gm (G2, Bb2, D2)
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=43, start=2.875, end=2.875 + 0.375),  # G2
    pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.25 + 0.375),  # Bb2
    pretty_midi.Note(velocity=80, pitch=38, start=3.625, end=3.625 + 0.375),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=4.0, end=4.0 + 0.375),  # C2 (chromatic approach)
])

# Bar 4: Cm (C2, Eb2, G2)
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=40, start=4.25, end=4.25 + 0.375),  # C2
    pretty_midi.Note(velocity=80, pitch=43, start=4.625, end=4.625 + 0.375),  # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=5.0, end=5.0 + 0.375),  # G2
    pretty_midi.Note(velocity=80, pitch=41, start=5.375, end=5.375 + 0.375),  # F2 (chromatic approach)
])

bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.5 + 0.15),  # D4
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.5 + 0.15),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.5 + 0.15),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.5 + 0.15),  # C5
]

# Bar 3: Gm7 (G, Bb, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.875, end=2.875 + 0.15),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=2.875, end=2.875 + 0.15),  # Bb4
    pretty_midi.Note(velocity=90, pitch=62, start=2.875, end=2.875 + 0.15),  # D4
    pretty_midi.Note(velocity=90, pitch=64, start=2.875, end=2.875 + 0.15),  # F4
])

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=4.25, end=4.25 + 0.15),  # C4
    pretty_midi.Note(velocity=90, pitch=63, start=4.25, end=4.25 + 0.15),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.25 + 0.15),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=4.25, end=4.25 + 0.15),  # Bb4
])

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - Eb4 - F4 - D4 (descending)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.5 + 0.375),  # D4
    pretty_midi.Note(velocity=110, pitch=63, start=1.875, end=1.875 + 0.375),  # Eb4
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.25 + 0.375),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.625 + 0.375),  # D4
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.0 + 0.375),  # D4 (return)
]

sax.notes.extend(sax_notes)

# Drums in bars 2-4: same pattern as bar 1
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick_time = start + 0.0
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)
    kick_time = start + 0.75
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare_time = start + 0.375
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)
    snare_time = start + 1.125
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat_time = start + i * 0.375
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
