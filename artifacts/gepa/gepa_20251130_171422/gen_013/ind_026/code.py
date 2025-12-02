
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante - Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Marcus - Bass
piano = pretty_midi.Instrument(program=0)      # Diane - Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray - Drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    time = bar * 1.5
    # Kick on beat 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375))
    # Snare on beat 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.75, end=time + 0.75 + 0.375))
    # Kick on beat 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time + 1.125, end=time + 1.125 + 0.375))
    # Snare on beat 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 1.5, end=time + 1.5 + 0.375))
    # Hi-hat on every eighth
    for i in range(8):
        hihat_start = time + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_start + 0.125))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm, chromatic approaches, never the same note twice
# Fm7: F, Ab, C, Eb
# Walk in Fm: F - Eb - D - C - Bb - A - G - F
# Bar 2: F - Eb - D - C
# Bar 3: Bb - A - G - F
# Bar 4: C - Bb - A - G

# Bass
for bar in range(2, 5):
    time = (bar - 2) * 1.5 + 1.5  # start at bar 2 (1.5s)
    for i in range(4):
        note_start = time + i * 0.375
        if bar == 2:
            note = ['F', 'Eb', 'D', 'C'][i]
        elif bar == 3:
            note = ['Bb', 'A', 'G', 'F'][i]
        elif bar == 4:
            note = ['C', 'Bb', 'A', 'G'][i]
        pitch = pretty_midi.note_name_to_number(note)
        bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=note_start, end=note_start + 0.375))

# Piano: 7th chords, comp on 2 and 4
# Fm7: F, Ab, C, Eb
# Bar 2: Fm7 on beat 1, rest
# Bar 3: Fm7 on beat 1, rest
# Bar 4: Fm7 on beat 1, rest
# Comp on 2 and 4: Fm7

# Bar 2: Fm7 on beat 1
piano.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_name_to_number('F'), start=1.5, end=1.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_name_to_number('Ab'), start=1.5, end=1.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_name_to_number('C'), start=1.5, end=1.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_name_to_number('Eb'), start=1.5, end=1.5 + 0.375))

# Bar 3: Fm7 on beat 1
piano.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_name_to_number('F'), start=3.0, end=3.0 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_name_to_number('Ab'), start=3.0, end=3.0 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_name_to_number('C'), start=3.0, end=3.0 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_name_to_number('Eb'), start=3.0, end=3.0 + 0.375))

# Bar 4: Fm7 on beat 1
piano.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_name_to_number('F'), start=4.5, end=4.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_name_to_number('Ab'), start=4.5, end=4.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_name_to_number('C'), start=4.5, end=4.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_name_to_number('Eb'), start=4.5, end=4.5 + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Eb - D - C (octave above), then rest, then repeat with a slight variation

# Bar 2: F, Eb, D, C (octave up)
for i in range(4):
    note = ['F', 'Eb', 'D', 'C'][i]
    pitch = pretty_midi.note_name_to_number(note) + 12
    start = 1.5 + i * 0.375
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# Bar 3: Rest

# Bar 4: F, Eb, D, C (octave up), but with a slight variation
for i in range(4):
    note = ['F', 'Eb', 'D', 'C'][i]
    pitch = pretty_midi.note_name_to_number(note) + 12
    start = 4.5 + i * 0.375
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# Add the final note with a slight delay to linger
sax.notes.append(pretty_midi.Note(velocity=100, pitch=pretty_midi.note_name_to_number('C') + 12, start=4.5 + 1.5, end=4.5 + 1.5 + 0.25))

# Add the rest of the drum pattern for bars 2-4
for bar in range(2, 5):
    time = (bar - 2) * 1.5 + 1.5  # start at bar 2 (1.5s)
    # Kick on beat 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375))
    # Snare on beat 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.75, end=time + 0.75 + 0.375))
    # Kick on beat 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time + 1.125, end=time + 1.125 + 0.375))
    # Snare on beat 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 1.5, end=time + 1.5 + 0.375))
    # Hi-hat on every eighth
    for i in range(8):
        hihat_start = time + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_start + 0.125))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("intro_in_Fm.mid")
