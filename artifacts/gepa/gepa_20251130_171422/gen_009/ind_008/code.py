
import pretty_midi

# Initialize the MIDI file with 160 BPM and 4/4 time
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum mappings
kick = 36
snare = 38
hihat = 42

# Time per bar in seconds (160 BPM, 4/4 time)
bar_length = 1.5  # 60 / 160 * 4 = 1.5s per bar

# Bar 1 (0.0 - 1.5s): Little Ray on drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(0, int(bar_length * 16) + 1, 1):  # 16 notes per bar at 160 BPM
    time = i / 16
    if time in [0.0, 0.75]:  # Kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=kick, start=i / 16, end=(i + 1) / 16)
        drums.notes.append(note)
    if time in [0.5, 1.25]:  # Snare on 2 and 4
        note = pretty_midi.Note(velocity=100, pitch=snare, start=i / 16, end=(i + 1) / 16)
        drums.notes.append(note)
    if i % 2 == 0:  # Hihat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=hihat, start=i / 16, end=(i + 1) / 16)
        drums.notes.append(note)

# Bar 2 (1.5 - 3.0s): Full quartet in
# Time offset for the start of this bar
offset = bar_length

# Bass line: Marcus on walking line with chromatic approaches
bass_notes = [
    (offset + 0.0, 37),  # F (root)
    (offset + 0.25, 36),  # Eb chromatic
    (offset + 0.5, 38),  # G (3rd)
    (offset + 0.75, 39),  # Ab chromatic
    (offset + 1.0, 40),  # A (5th)
    (offset + 1.25, 41),  # Bb chromatic
    (offset + 1.5, 42),  # B (7th)
    (offset + 1.75, 43)  # C chromatic
]

for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: Diane on 7th chords, comp on 2 and 4
# Bar 2: 7th chord on F7 (F, A, C, Eb)
piano_notes = [
    (offset + 0.0, 53),  # F (root)
    (offset + 0.0, 60),  # A (3rd)
    (offset + 0.0, 64),  # C (5th)
    (offset + 0.0, 62),  # Eb (7th)
    (offset + 0.5, 60),  # A (3rd)
    (offset + 0.5, 67),  # C (5th)
    (offset + 0.5, 65),  # Eb (7th)
    (offset + 0.5, 68)   # F (8th)
]

for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25)
    piano.notes.append(note)

# Sax: Dante's motif (first iteration)
# F -> G -> Ab -> F, with space and tension
sax_notes = [
    (offset + 0.0, 65),  # F
    (offset + 0.25, 67),  # G
    (offset + 0.5, 69),  # Ab
    (offset + 0.75, 65)   # F
]

for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

# Bar 3 (3.0 - 4.5s): Continue the pattern
# Bass: Same walking line, shifted
bass_notes = [
    (offset + 1.5, 37),  # F
    (offset + 1.75, 36),  # Eb
    (offset + 2.0, 38),  # G
    (offset + 2.25, 39),  # Ab
    (offset + 2.5, 40),  # A
    (offset + 2.75, 41),  # Bb
    (offset + 3.0, 42),  # B
    (offset + 3.25, 43)  # C
]

for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: 7th chord on F7 again
piano_notes = [
    (offset + 1.5, 53),  # F
    (offset + 1.5, 60),  # A
    (offset + 1.5, 64),  # C
    (offset + 1.5, 62),  # Eb
    (offset + 2.0, 60),  # A
    (offset + 2.0, 67),  # C
    (offset + 2.0, 65),  # Eb
    (offset + 2.0, 68)   # F
]

for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25)
    piano.notes.append(note)

# Sax: Play the motif again, with a slight variation
sax_notes = [
    (offset + 1.5, 65),  # F
    (offset + 1.75, 67),  # G
    (offset + 2.0, 69),  # Ab
    (offset + 2.25, 67)  # G
]

for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

# Bar 4 (4.5 - 6.0s): Final bar
# Bass: Same line again
bass_notes = [
    (offset + 3.0, 37),  # F
    (offset + 3.25, 36),  # Eb
    (offset + 3.5, 38),  # G
    (offset + 3.75, 39),  # Ab
    (offset + 4.0, 40),  # A
    (offset + 4.25, 41),  # Bb
    (offset + 4.5, 42),  # B
    (offset + 4.75, 43)  # C
]

for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: 7th chord again
piano_notes = [
    (offset + 3.0, 53),  # F
    (offset + 3.0, 60),  # A
    (offset + 3.0, 64),  # C
    (offset + 3.0, 62),  # Eb
    (offset + 3.5, 60),  # A
    (offset + 3.5, 67),  # C
    (offset + 3.5, 65),  # Eb
    (offset + 3.5, 68)   # F
]

for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25)
    piano.notes.append(note)

# Sax: Final iteration, leaving it hanging
sax_notes = [
    (offset + 3.0, 65),  # F
    (offset + 3.25, 67),  # G
    (offset + 3.5, 69),  # Ab
    (offset + 3.75, 69)  # Ab (sustained)
]

for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
