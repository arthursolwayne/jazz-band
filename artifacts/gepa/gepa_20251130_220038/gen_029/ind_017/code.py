
import pretty_midi

# Initialize the MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments for each player
sax = pretty_midi.Instrument(program=66)       # Tenor sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Define drum notes
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            # Kick on 1 and 3
            note = pretty_midi.Note(velocity=90, pitch=kick, start=time, end=time + 0.125)
            drums.notes.append(note)
        elif beat == 1 or beat == 3:
            # Snare on 2 and 4
            note = pretty_midi.Note(velocity=90, pitch=snare, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hihat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=hihat, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=49, start=2.5, end=2.75),  # B
    pretty_midi.Note(velocity=80, pitch=50, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=80, pitch=48, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=47, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=46, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=80, pitch=45, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=80, pitch=44, start=4.25, end=4.5),  # E
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=80, pitch=43, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=80, pitch=45, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=5.75, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
# Key: F7 = F A C E
# Comp on beats 2 and 4 of each bar
chords = {
    1.5: [pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.625)],  # F
    1.75: [pretty_midi.Note(velocity=90, pitch=58, start=1.75, end=1.875)], # A
    2.0: [pretty_midi.Note(velocity=90, pitch=55, start=2.0, end=2.125)],  # C
    2.25: [pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.375)], # E
    3.0: [pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.125)],  # F
    3.25: [pretty_midi.Note(velocity=90, pitch=58, start=3.25, end=3.375)], # A
    3.5: [pretty_midi.Note(velocity=90, pitch=55, start=3.5, end=3.625)],  # C
    3.75: [pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=3.875)], # E
    4.5: [pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.625)],  # F
    4.75: [pretty_midi.Note(velocity=90, pitch=58, start=4.75, end=4.875)], # A
    5.0: [pretty_midi.Note(velocity=90, pitch=55, start=5.0, end=5.125)],  # C
    5.25: [pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.375)], # E
}
for time, notes in chords.items():
    for note in notes:
        piano.notes.append(note)

# Sax (Dante): Motif in F, start it, leave it hanging, come back and finish it
# Motif: F, E, Bb, F (a simple melodic idea, no scale runs)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=100, pitch=48, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=2.5, end=2.75),  # F (return)
    pretty_midi.Note(velocity=100, pitch=51, start=2.75, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=48, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=100, pitch=48, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=5.75, end=6.0)   # E
]
sax.notes.extend(sax_notes)

# Drums (Little Ray): Same as in Bar 1, repeated for bars 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            # Kick on 1 and 3
            note = pretty_midi.Note(velocity=90, pitch=kick, start=time, end=time + 0.125)
            drums.notes.append(note)
        elif beat == 1 or beat == 3:
            # Snare on 2 and 4
            note = pretty_midi.Note(velocity=90, pitch=snare, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hihat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=hihat, start=time, end=time + 0.125)
        drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_4_bar_intro.mid")
