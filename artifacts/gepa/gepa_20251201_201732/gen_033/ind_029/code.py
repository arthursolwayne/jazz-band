
import pretty_midi

# Initialize the MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    end = start + 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    # Add kick and snare
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Time signature: 4/4, 160 BPM, bar duration = 1.5s

# Bass (Marcus): Walking line in Fm, roots and fifths with chromatic approaches
# Fm root = 53 (F), fifth = 58 (C)
# Chromatic approach: 52 (E), 59 (C#)
for bar in range(2, 5):
    start = bar * 1.5
    end = start + 1.5
    # Bass line: E, F, C#, C, F, E, Bb, Bb
    notes = [
        pretty_midi.Note(velocity=80, pitch=52, start=start, end=start + 0.375),     # E
        pretty_midi.Note(velocity=80, pitch=53, start=start + 0.375, end=start + 0.75),  # F
        pretty_midi.Note(velocity=80, pitch=59, start=start + 0.75, end=start + 1.125),  # C#
        pretty_midi.Note(velocity=80, pitch=58, start=start + 1.125, end=start + 1.5),   # C
    ]
    # Repeat for next bar
    if bar == 2:
        notes.extend([
            pretty_midi.Note(velocity=80, pitch=53, start=start + 1.5, end=start + 1.875), # F
            pretty_midi.Note(velocity=80, pitch=52, start=start + 1.875, end=start + 2.25), # E
            pretty_midi.Note(velocity=80, pitch=57, start=start + 2.25, end=start + 2.625), # Bb
            pretty_midi.Note(velocity=80, pitch=57, start=start + 2.625, end=start + 3.0),  # Bb
        ])
    if bar == 3:
        notes.extend([
            pretty_midi.Note(velocity=80, pitch=53, start=start + 1.5, end=start + 1.875), # F
            pretty_midi.Note(velocity=80, pitch=52, start=start + 1.875, end=start + 2.25), # E
            pretty_midi.Note(velocity=80, pitch=57, start=start + 2.25, end=start + 2.625), # Bb
            pretty_midi.Note(velocity=80, pitch=57, start=start + 2.625, end=start + 3.0),  # Bb
        ])
    bass.notes.extend(notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
# Bar 3: Gm7 (G, Bb, D, F)
# Bar 4: Cm7 (C, Eb, G, Bb)
for bar in range(2, 5):
    start = bar * 1.5
    end = start + 1.5
    if bar == 2:
        # Fm7 (F, Ab, C, Eb)
        notes = [
            pretty_midi.Note(velocity=100, pitch=53, start=start, end=end),   # F
            pretty_midi.Note(velocity=100, pitch=60, start=start, end=end),   # Ab
            pretty_midi.Note(velocity=100, pitch=58, start=start, end=end),   # C
            pretty_midi.Note(velocity=100, pitch=62, start=start, end=end),   # Eb
        ]
    elif bar == 3:
        # Gm7 (G, Bb, D, F)
        notes = [
            pretty_midi.Note(velocity=100, pitch=55, start=start, end=end),   # G
            pretty_midi.Note(velocity=100, pitch=57, start=start, end=end),   # Bb
            pretty_midi.Note(velocity=100, pitch=62, start=start, end=end),   # D
            pretty_midi.Note(velocity=100, pitch=53, start=start, end=end),   # F
        ]
    elif bar == 4:
        # Cm7 (C, Eb, G, Bb)
        notes = [
            pretty_midi.Note(velocity=100, pitch=58, start=start, end=end),   # C
            pretty_midi.Note(velocity=100, pitch=62, start=start, end=end),   # Eb
            pretty_midi.Note(velocity=100, pitch=55, start=start, end=end),   # G
            pretty_midi.Note(velocity=100, pitch=57, start=start, end=end),   # Bb
        ]
    piano.notes.extend(notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Eb, C — play on beat 1 and 3 of bar 2, then end on beat 3 of bar 4
for bar in [2, 3]:
    start = bar * 1.5
    if bar == 2:
        # Play on beat 1 (start + 0.0)
        notes = [
            pretty_midi.Note(velocity=100, pitch=53, start=start, end=start + 0.375),  # F
            pretty_midi.Note(velocity=100, pitch=60, start=start + 1.125, end=start + 1.5),  # Eb
        ]
    elif bar == 3:
        # Play on beat 3 (start + 1.125)
        notes = [
            pretty_midi.Note(velocity=100, pitch=62, start=start + 1.125, end=start + 1.5),  # C
        ]
    sax.notes.extend(notes)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    end = start + 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    # Add kick and snare
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
