
import pretty_midi

# Initialize MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes (kick=36, snare=38, hihat=42)
kick = 36
snare = 38
hihat = 42

# Bar length in seconds (160 BPM, 4/4 time)
bar_length = 1.5  # 6 seconds for 4 bars

# Bar 1: DRUMS ONLY (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    time = bar * bar_length
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=kick, start=time + 0.0, end=time + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=kick, start=time + 0.75, end=time + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=snare, start=time + 0.375, end=time + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=snare, start=time + 1.125, end=time + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=hihat, start=time + 0.0, end=time + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=hihat, start=time + 0.375, end=time + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=hihat, start=time + 0.75, end=time + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=hihat, start=time + 1.125, end=time + 1.5)
    # Add to drums instrument
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

# Bar 2: INTRO (1.5 - 3.0s)
# Marcus: Walking bass line in D minor, chromatic approaches
# Dm7: D, F, A, C
# Walking line: D -> C -> B -> A -> G -> F -> E -> D -> C -> B -> A -> G -> F -> E -> D
# Notes in D minor: D, Eb, F, G, A, Bb, C

# Bass line
bass_notes = [
    (1.5, 62),   # D
    (1.875, 60), # C
    (2.25, 61),  # B
    (2.625, 59), # A
    (3.0, 60),   # G
]

for note in bass_notes:
    start, pitch = note
    bass_note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Diane: Piano comping on 2 and 4
# Dm7: D, F, A, C
# Comp on 2 and 4: chords on beats 2 and 4

# Bar 2: beat 2
piano_note = pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25)
piano.notes.append(piano_note)
# Bar 2: beat 4
piano_note = pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375)
piano.notes.append(piano_note)

# Little Ray: Same as bar 1 but in bar 2
for bar in range(1):
    time = bar * bar_length + 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=kick, start=time + 0.0, end=time + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=kick, start=time + 0.75, end=time + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=snare, start=time + 0.375, end=time + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=snare, start=time + 1.125, end=time + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=hihat, start=time + 0.0, end=time + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=hihat, start=time + 0.375, end=time + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=hihat, start=time + 0.75, end=time + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=hihat, start=time + 1.125, end=time + 1.5)
    # Add to drums instrument
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

# Bar 3: Dante on sax, start motif
# Melody in D minor, short motif: D -> Eb -> F -> C
# Notes: D (62), Eb (63), F (65), C (60)

# Start motif at 3.0s
motif_start = 3.0
motif_end = 3.0 + 0.75  # 3 notes, 0.25s each

# Start D
note = pretty_midi.Note(velocity=100, pitch=62, start=motif_start, end=motif_start + 0.25)
sax.notes.append(note)

# Eb
note = pretty_midi.Note(velocity=100, pitch=63, start=motif_start + 0.25, end=motif_start + 0.5)
sax.notes.append(note)

# F
note = pretty_midi.Note(velocity=100, pitch=65, start=motif_start + 0.5, end=motif_start + 0.75)
sax.notes.append(note)

# Bar 4: Futile attempt to resolve (leave it hanging)
# Play the same motif again, but not resolve

# Play again at 3.75s
note = pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=63, start=4.0, end=4.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5)
sax.notes.append(note)

# Add full instruments
# Bar 3 and 4: Full quartet
# Marcus: Continue walking bass
# Walking line: G -> F -> E -> D -> C -> B -> A -> G -> F -> E -> D -> C -> B -> A -> G

# Bar 3: G -> F -> E -> D
bass_notes = [
    (3.0, 60),   # G
    (3.375, 60), # F
    (3.75, 60),  # E
    (4.125, 60), # D
]

for note in bass_notes:
    start, pitch = note
    bass_note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Diane: Comp on 2 and 4
# Bar 3: beat 2 and 4
piano_note = pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875)
piano.notes.append(piano_note)

# Bar 4: beat 2 and 4
piano_note = pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=62, start=6.0, end=6.375)
piano.notes.append(piano_note)

# Little Ray: Same pattern on bar 3 and 4
for bar in range(2):
    time = bar * bar_length + 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=kick, start=time + 0.0, end=time + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=kick, start=time + 0.75, end=time + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=snare, start=time + 0.375, end=time + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=snare, start=time + 1.125, end=time + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=hihat, start=time + 0.0, end=time + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=hihat, start=time + 0.375, end=time + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=hihat, start=time + 0.75, end=time + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=hihat, start=time + 1.125, end=time + 1.5)
    # Add to drums instrument
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write("dante_intro.mid")
