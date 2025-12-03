
import pretty_midi

# Initialize MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instrumetns
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42
# Define MIDI note numbers for key F (F=65)
F = 65
# Other notes in F major: G (67), A (69), Bb (70), B (71), C (60), D (62), E (64)

# BAR 1: DRUMS ALONE (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = beat * 0.375  # 0.375 seconds per beat
    if beat % 2 == 0:
        # Kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        # Snare on 2 and 4
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    # Hi-hat on every eighth
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
    drums.notes.append(note)

# BAR 2: FULL QUARTET (1.5 - 3.0s)
# Diane (piano): Open voicings, different chord each bar
# Bar 2: Fmaj7 (F, A, C, E)
note = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.5 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.5 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.5 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + 0.25)
piano.notes.append(note)

# Marcus (bass): Walking line, roots and fifths with chromatic approaches
# Bar 2: F (65) -> G (67) -> Bb (70) -> C (60)
note = pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.5 + 0.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=1.75 + 0.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=70, start=2.0, end=2.0 + 0.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.25 + 0.25)
bass.notes.append(note)

# Dante (sax): Start the motif (F -> G -> Ab -> F)
note = pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.5 + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.75 + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.0 + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.25 + 0.25)
sax.notes.append(note)

# BAR 3: FULL QUARTET (3.0 - 4.5s)
# Diane (piano): Bbmaj7 (Bb, D, F, Ab)
note = pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.0 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.0 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.0 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.0 + 0.25)
piano.notes.append(note)

# Marcus (bass): Bb (70) -> C (60) -> D (62) -> Eb (64)
note = pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.0 + 0.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.25 + 0.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.5 + 0.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=3.75 + 0.25)
bass.notes.append(note)

# Dante (sax): Continue the motif (F -> G -> Ab -> F)
note = pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.0 + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.25 + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.5 + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=3.75 + 0.25)
sax.notes.append(note)

# BAR 4: FULL QUARTET (4.5 - 6.0s)
# Diane (piano): C7 (C, E, G, Bb)
note = pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.5 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.5 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.5 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.5 + 0.25)
piano.notes.append(note)

# Marcus (bass): C (60) -> D (62) -> Eb (64) -> F (65)
note = pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.5 + 0.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=4.75 + 0.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.0 + 0.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.25 + 0.25)
bass.notes.append(note)

# Dante (sax): Finish the motif (F -> G -> Ab -> F)
note = pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.5 + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=4.75 + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.0 + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.25 + 0.25)
sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.append(sax)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)

# Save the MIDI file
# midi.write disabled
