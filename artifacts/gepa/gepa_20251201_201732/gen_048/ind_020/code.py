
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    midi_time = start + 0.0
    note = pretty_midi.Note(velocity=100, pitch=36, start=midi_time, end=midi_time + 0.1)
    drums.notes.append(note)
    midi_time = start + 0.75
    note = pretty_midi.Note(velocity=100, pitch=36, start=midi_time, end=midi_time + 0.1)
    drums.notes.append(note)
    # Snare on 2 and 4
    midi_time = start + 0.375
    note = pretty_midi.Note(velocity=110, pitch=38, start=midi_time, end=midi_time + 0.1)
    drums.notes.append(note)
    midi_time = start + 1.125
    note = pretty_midi.Note(velocity=110, pitch=38, start=midi_time, end=midi_time + 0.1)
    drums.notes.append(note)
    # Hihat on every eighth
    for i in range(8):
        midi_time = start + i * 0.375
        note = pretty_midi.Note(velocity=90, pitch=42, start=midi_time, end=midi_time + 0.05)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: walking line, roots and fifths with chromatic approaches
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Fm7: F, C, Ab, D
        # Root F (40)
        note = pretty_midi.Note(velocity=90, pitch=40, start=start, end=start + 0.25)
        bass.notes.append(note)
        # Chromatic approach to C (43)
        note = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1)
        bass.notes.append(note)
        note = pretty_midi.Note(velocity=90, pitch=43, start=start + 0.1, end=start + 0.25)
        bass.notes.append(note)
    elif bar == 3:
        # Am7: A, E, C, G
        # Root A (45)
        note = pretty_midi.Note(velocity=90, pitch=45, start=start, end=start + 0.25)
        bass.notes.append(note)
        # Chromatic approach to E (48)
        note = pretty_midi.Note(velocity=80, pitch=47, start=start, end=start + 0.1)
        bass.notes.append(note)
        note = pretty_midi.Note(velocity=90, pitch=48, start=start + 0.1, end=start + 0.25)
        bass.notes.append(note)
    elif bar == 4:
        # D7: D, A, F#, C
        # Root D (50)
        note = pretty_midi.Note(velocity=90, pitch=50, start=start, end=start + 0.25)
        bass.notes.append(note)
        # Chromatic approach to A (53)
        note = pretty_midi.Note(velocity=80, pitch=52, start=start, end=start + 0.1)
        bass.notes.append(note)
        note = pretty_midi.Note(velocity=90, pitch=53, start=start + 0.1, end=start + 0.25)
        bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Fm7: F, A, C, Eb
        note = pretty_midi.Note(velocity=100, pitch=40, start=start, end=start + 0.5)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=45, start=start, end=start + 0.5)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=43, start=start, end=start + 0.5)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=41, start=start, end=start + 0.5)
        piano.notes.append(note)
    elif bar == 3:
        # Am7: A, C, E, G
        note = pretty_midi.Note(velocity=100, pitch=45, start=start, end=start + 0.5)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=48, start=start, end=start + 0.5)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=50, start=start, end=start + 0.5)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=47, start=start, end=start + 0.5)
        piano.notes.append(note)
    elif bar == 4:
        # D7: D, F#, A, C
        note = pretty_midi.Note(velocity=100, pitch=50, start=start, end=start + 0.5)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=53, start=start, end=start + 0.5)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=55, start=start, end=start + 0.5)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=52, start=start, end=start + 0.5)
        piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, F
# Bar 2: F (40) on beat 1, Ab (41) on beat 2, Bb (42) on beat 3, F (40) on beat 4
# Bar 4: F (40) on beat 1, Ab (41) on beat 2, Bb (42) on beat 3, F (40) on beat 4

# Bar 2
start = 1.5
note = pretty_midi.Note(velocity=110, pitch=40, start=start, end=start + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=41, start=start + 0.375, end=start + 0.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=42, start=start + 0.75, end=start + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=40, start=start + 1.125, end=start + 1.5)
sax.notes.append(note)

# Bar 4
start = 4.5
note = pretty_midi.Note(velocity=110, pitch=40, start=start, end=start + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=41, start=start + 0.375, end=start + 0.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=42, start=start + 0.75, end=start + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=40, start=start + 1.125, end=start + 1.5)
sax.notes.append(note)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    midi_time = start + 0.0
    note = pretty_midi.Note(velocity=100, pitch=36, start=midi_time, end=midi_time + 0.1)
    drums.notes.append(note)
    midi_time = start + 0.75
    note = pretty_midi.Note(velocity=100, pitch=36, start=midi_time, end=midi_time + 0.1)
    drums.notes.append(note)
    # Snare on 2 and 4
    midi_time = start + 0.375
    note = pretty_midi.Note(velocity=110, pitch=38, start=midi_time, end=midi_time + 0.1)
    drums.notes.append(note)
    midi_time = start + 1.125
    note = pretty_midi.Note(velocity=110, pitch=38, start=midi_time, end=midi_time + 0.1)
    drums.notes.append(note)
    # Hihat on every eighth
    for i in range(8):
        midi_time = start + i * 0.375
        note = pretty_midi.Note(velocity=90, pitch=42, start=midi_time, end=midi_time + 0.05)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
