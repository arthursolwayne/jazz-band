
import pretty_midi

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Key: F minor
Fm = pretty_midi.key_number_from_key_signature("Fm")

# Time signature: 4/4
midi.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Bar 1: Little Ray on drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    end = start + 1.5

    # Kick on 1 and 3
    kick_times = [start + 0.0, start + 0.75]  # 1 and 3
    for time in kick_times:
        note = pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.1)
        drums.notes.append(note)

    # Snare on 2 and 4
    snare_times = [start + 0.375, start + 1.125]  # 2 and 4
    for time in snare_times:
        note = pretty_midi.Note(velocity=110, pitch=SNARE, start=time, end=time + 0.1)
        drums.notes.append(note)

    # Hi-hat on every eighth
    hihat_times = [start + t * 0.375 for t in range(4)]
    for time in hihat_times:
        note = pretty_midi.Note(velocity=80, pitch=HIHAT, start=time, end=time + 0.1)
        drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
# Walking line in Fm, chromatic approaches
bass_notes = [
    (1.5, 72),     # F (C4)
    (1.875, 71),   # E (Bb4)
    (2.25, 72),    # F (C4)
    (2.625, 73),   # G (Db4)
    (3.0, 71),     # E (Bb4)
    (3.375, 72),   # F (C4)
    (3.75, 73),    # G (Db4)
    (4.125, 74),   # A (Eb4)
    (4.5, 73),     # G (Db4)
    (4.875, 72),   # F (C4)
    (5.25, 71),    # E (Bb4)
    (5.625, 72),   # F (C4)
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano (Diane)
# 7th chords comping on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bb7 = Bb, D, F, Ab
# Gm7 = G, Bb, D, F
# Amaj7 = A, C#, E, G
piano_notes = [
    # Bar 2: Fm7 on 2nd beat
    (2.25, 72),  # F
    (2.25, 69),  # Ab
    (2.25, 72),  # C
    (2.25, 67),  # Eb

    # Bar 2: Bb7 on 4th beat
    (3.0, 71),   # Bb
    (3.0, 67),   # D
    (3.0, 72),   # F
    (3.0, 69),   # Ab

    # Bar 3: Gm7 on 2nd beat
    (3.75, 73),  # G
    (3.75, 71),  # Bb
    (3.75, 67),  # D
    (3.75, 72),  # F

    # Bar 3: Amaj7 on 4th beat
    (4.5, 74),   # A
    (4.5, 76),   # C#
    (4.5, 69),   # E
    (4.5, 73),   # G

    # Bar 4: Fm7 on 2nd beat
    (5.25, 72),  # F
    (5.25, 69),  # Ab
    (5.25, 72),  # C
    (5.25, 67),  # Eb

    # Bar 4: Bb7 on 4th beat
    (5.625, 71), # Bb
    (5.625, 67), # D
    (5.625, 72), # F
    (5.625, 69), # Ab
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Saxophone (Dante)
# One short motif, make it sing
# Start on G (73) on beat 2 of bar 2 (1.875s)
# Motif: G -> F -> E -> G (sings Fm)
# Use a legato feel, no scale runs

# First note: G (73) on 1.875s
sax_note = pretty_midi.Note(velocity=105, pitch=73, start=1.875, end=2.125)
sax.notes.append(sax_note)

# Second note: F (72) on 2.25s
sax_note = pretty_midi.Note(velocity=105, pitch=72, start=2.25, end=2.5)
sax.notes.append(sax_note)

# Third note: E (71) on 2.625s
sax_note = pretty_midi.Note(velocity=105, pitch=71, start=2.625, end=2.875)
sax.notes.append(sax_note)

# Final note: G (73) on 3.0s
sax_note = pretty_midi.Note(velocity=105, pitch=73, start=3.0, end=3.25)
sax.notes.append(sax_note)

# Add instruments to the MIDI file
midi.instruments = [sax, bass, piano, drums]

# Save the MIDI file
midi.write("dante_intro.mid")
