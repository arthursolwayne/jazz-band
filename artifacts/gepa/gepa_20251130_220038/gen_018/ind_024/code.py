
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante on tenor sax
bass = pretty_midi.Instrument(program=33)      # Marcus on bass
piano = pretty_midi.Instrument(program=0)      # Diane on piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray on drums

# Drum mappings
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 1, 2, 3]:
    time = beat * 0.375
    if beat % 2 == 0:  # Kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.375)
        drums.notes.append(note)
    else:  # Snare on 2 and 4
        note = pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.375)
        drums.notes.append(note)
    # Hi-hat on every eighth
    note = pretty_midi.Note(velocity=80, pitch=HIHAT, start=time, end=time + 0.375)
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
# D minor key, walking in D Dorian (D, E, F, G, A, B, C)
# Start at D (62), walk up with chromatic approach to E (64)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),   # D
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.25),  # C#
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),   # F#
    pretty_midi.Note(velocity=80, pitch=68, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),  # G#
    pretty_midi.Note(velocity=80, pitch=70, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5),   # A#
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.875),   # B
    pretty_midi.Note(velocity=80, pitch=73, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625),  # A#
    pretty_midi.Note(velocity=80, pitch=72, start=5.625, end=6.0),   # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# D7 (D, F#, A, C) - root position
# D7 (D, F#, A, C) - first inversion
# D7 (D, F#, A, C) - second inversion (A, C, D, F#)
# D7 (D, F#, A, C) - third inversion (C, D, F#, A)
# Comp on beats 2 and 4 of each bar

def add_piano_chord(note_list, time):
    for pitch in note_list:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.375)
        piano.notes.append(note)

chord_D7 = [62, 65, 68, 70]  # D, F#, A, C
chord_D7_inv1 = [68, 70, 62, 65]  # A, C, D, F#
chord_D7_inv2 = [70, 62, 65, 68]  # C, D, F#, A
chord_D7_inv3 = [62, 65, 68, 70]  # Root position again

# Bar 2 (1.5 - 3.0s)
add_piano_chord(chord_D7_inv3, 1.5)  # Comp on 2
add_piano_chord(chord_D7_inv1, 2.25) # Comp on 4

# Bar 3 (3.0 - 4.5s)
add_piano_chord(chord_D7_inv2, 3.0)  # Comp on 2
add_piano_chord(chord_D7_inv3, 3.75) # Comp on 4

# Bar 4 (4.5 - 6.0s)
add_piano_chord(chord_D7_inv1, 4.5)  # Comp on 2
add_piano_chord(chord_D7_inv2, 5.25) # Comp on 4

# Sax: Tenor sax motif — short, singable, one idea, leave it hanging
# D (62), F# (65), G (67), B (70) — the motif
# Play the first two notes, leave the last two for the next bar

note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25)
note3 = pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625)
note4 = pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=3.0)

sax.notes.extend([note1, note2, note3, note4])

# Now add the full motif again in bar 4 (complete it)
note5 = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875)
note6 = pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25)
note7 = pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625)
note8 = pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0)

sax.notes.extend([note5, note6, note7, note8])

# Drums: Continue with the same pattern (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
for bar in range(2, 4):  # bars 2, 3
    start_time = bar * 1.5
    for beat in [0, 1, 2, 3]:
        time = start_time + beat * 0.375
        if beat % 2 == 0:  # Kick on 1 and 3
            note = pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.375)
            drums.notes.append(note)
        else:  # Snare on 2 and 4
            note = pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.375)
            drums.notes.append(note)
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=HIHAT, start=time, end=time + 0.375)
        drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_introduction.mid")
