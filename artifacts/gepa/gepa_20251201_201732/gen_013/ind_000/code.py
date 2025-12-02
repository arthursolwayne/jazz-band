
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
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass in Fm (F - Ab - Bb - Db)
# Roots and fifths with chromatic approaches
# Bar 2: F - Ab - Bb - Db
# Bar 3: Ab - Bb - Db - F
# Bar 4: Bb - Db - F - Ab

for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        notes = [38, 41, 42, 45]  # F2 (38), Ab2 (41), Bb2 (42), Db2 (45)
    elif bar == 3:
        notes = [41, 42, 45, 38]  # Ab2 (41), Bb2 (42), Db2 (45), F2 (38)
    elif bar == 4:
        notes = [42, 45, 38, 41]  # Bb2 (42), Db2 (45), F2 (38), Ab2 (41)
    for i, note in enumerate(notes):
        # Walking bass on 1, 2, 3, 4
        duration = 0.375
        start_time = start + i * duration
        bass_note = pretty_midi.Note(velocity=100, pitch=note, start=start_time, end=start_time + duration)
        bass.notes.append(bass_note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
# Bar 3: Ab7 (Ab, C, Eb, G)
# Bar 4: Bb7 (Bb, D, F, Ab)

for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        notes = [38, 41, 48, 50]  # F, Ab, C, Eb
    elif bar == 3:
        notes = [41, 48, 50, 55]  # Ab, C, Eb, G
    elif bar == 4:
        notes = [42, 46, 48, 50]  # Bb, D, F, Ab
    # Diane plays on 2 and 4
    for i, note in enumerate(notes):
        if i == 1 or i == 3:
            duration = 0.75
            start_time = start + (i % 2) * 0.75
            piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start_time, end=start_time + duration)
            piano.notes.append(piano_note)

# Dante: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Ab - Bb - F (1 bar), then repeat with slight variation
# Bar 2: F, Ab, Bb, F
# Bar 3: F, Ab, Bb, Eb
# Bar 4: F, Ab, Bb, F

for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        notes = [38, 41, 42, 38]  # F, Ab, Bb, F
    elif bar == 3:
        notes = [38, 41, 42, 50]  # F, Ab, Bb, Eb
    elif bar == 4:
        notes = [38, 41, 42, 38]  # F, Ab, Bb, F
    for i, note in enumerate(notes):
        duration = 0.375
        start_time = start + i * duration
        sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start_time, end=start_time + duration)
        sax.notes.append(sax_note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
