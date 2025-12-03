
import pretty_midi

# Initialize the MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Bar duration in seconds (160 BPM, 4/4 time)
BAR_DURATION = 1.5

# Start with Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def setup_bar_one():
    time = 0.0

    # Kick on 1 and 3 (0.0 and 0.75s)
    kick_1 = pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.125)
    kick_3 = pretty_midi.Note(velocity=100, pitch=KICK, start=0.75, end=0.875)
    drums.notes.extend([kick_1, kick_3])

    # Snare on 2 and 4 (0.375 and 1.125s)
    snare_2 = pretty_midi.Note(velocity=90, pitch=SNARE, start=0.375, end=0.5)
    snare_4 = pretty_midi.Note(velocity=90, pitch=SNARE, start=1.125, end=1.25)
    drums.notes.extend([snare_2, snare_4])

    # Hi-hat on every eighth note
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=HIHAT, start=i * 0.125, end=i * 0.125 + 0.0625)
        drums.notes.append(hihat)

# Bar 2 to Bar 4 (1.5 to 6.0s) - Full quartet

# Bass line: Walking line in Fm (F, Ab, D, C, F, Ab, D, C)
def setup_bass_line():
    notes = [
        (1.5, 53),  # F2
        (1.75, 50), # Ab2
        (2.0, 55),  # D2
        (2.25, 52), # C2
        (2.5, 53),  # F2
        (2.75, 50), # Ab2
        (3.0, 55),  # D2
        (3.25, 52), # C2
        (3.5, 53),  # F2
        (3.75, 50), # Ab2
        (4.0, 55),  # D2
        (4.25, 52), # C2
        (4.5, 53),  # F2
        (4.75, 50), # Ab2
        (5.0, 55),  # D2
        (5.25, 52), # C2
    ]
    for start, note in notes:
        bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.25)
        bass.notes.append(bass_note)

# Piano chords: Open voicings, resolve on last beat of each bar
def setup_piano_chords():
    # Bar 2: Fm7 (F, Ab, C, D)
    # Bar 3: G7 (G, B, D, F)
    # Bar 4: Cm7 (C, Eb, G, Bb)
    chords = [
        (1.5, [53, 50, 57, 55]),  # Fm7
        (2.0, [58, 62, 55, 53]),  # G7
        (2.5, [57, 59, 62, 60]),  # Cm7
        (3.0, [58, 62, 55, 53]),  # G7
        (3.5, [57, 59, 62, 60]),  # Cm7
        (4.0, [53, 50, 57, 55]),  # Fm7
        (4.5, [58, 62, 55, 53]),  # G7
        (5.0, [57, 59, 62, 60]),  # Cm7
    ]
    for start, pitches in chords:
        for pitch in pitches:
            note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.5)
            piano.notes.append(note)

# Sax melody: Short motif, starts on 1st beat of bar 2, leaves it hanging, finishes on bar 4
def setup_sax_melody():
    # Start on F (53)
    # Motif: F -> Ab -> C -> D (up chromatic, then resolve) over bars 2-4
    # Notes:
    # Bar 2: F at 1.5s (1/2 note)
    # Bar 3: Ab at 2.75s (1/2 note)
    # Bar 4: C at 4.0s (1/2 note), D at 4.5s (1/2 note)
    # Total: F -> Ab -> C -> D
    sax_notes = [
        (1.5, 53, 1.0),  # F (1/2 note)
        (2.75, 50, 1.0), # Ab (1/2 note)
        (4.0, 57, 0.5),  # C (1/4 note)
        (4.5, 55, 0.5),  # D (1/4 note)
    ]
    for start, pitch, duration in sax_notes:
        sax_note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
        sax.notes.append(sax_note)

# Drum pattern for bars 2-4: Same as bar 1, just shifted
def setup_drums_bars_2_4():
    # Copy previous pattern but starting at 1.5s
    for note in drums.notes:
        note.start += 1.5
        note.end += 1.5

# Execute setups
setup_bar_one()
setup_bass_line()
setup_piano_chords()
setup_sax_melody()
setup_drums_bars_2_4()

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
