
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass - Marcus (Walking line, roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=3.0),   # F
]
bass.notes.extend(bass_notes)

# Piano - Diane (Open voicings, different chord each bar, resolve on the last)
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # Eb
]
piano.notes.extend(piano_notes)

# Sax - Dante (Motif: A - Bb - G - F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375),   # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass - Marcus (Walking line)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),   # F
]
bass.notes.extend(bass_notes)

# Piano - Diane (Open voicings, different chord each bar, resolve on the last)
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375),  # Ab
]
piano.notes.extend(piano_notes)

# Sax - Dante (Motif continuation)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),   # F
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass - Marcus (Walking line)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=41, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano - Diane (Open voicings, different chord each bar, resolve on the last)
# Bar 4: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Eb
]
piano.notes.extend(piano_notes)

# Sax - Dante (Motif resolution)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0),   # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
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
    start = bar * 1.5
    snare_start = start + 0.75
    snare_end = snare_start + 0.375
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end)
    drums.notes.append(snare)
    snare_start = start + 2.25
    snare_end = snare_start + 0.375
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end)
    drums.notes.append(snare)

# Hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    for i in range(8):
        hihat_start = start + i * 0.375
        hihat_end = hihat_start + 0.375
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_end)
        drums.notes.append(hihat)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("waynes_shot.mid")
