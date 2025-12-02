
import pretty_midi

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key: F minor (F, Gb, Ab, Bb, B, Db, Eb)
# We'll use F minor scale for reference, but the melody will be sparse and expressive.

# Time signature: 4/4
pm.time_signature_changes[0].numerator = 4
pm.time_signature_changes[0].denominator = 4

# Define the time for each bar (6 seconds for 4 bars at 160 BPM)
BAR_DURATION = 6.0 / 4  # 1.5 seconds per bar
BEAT_DURATION = 0.375  # 0.375 seconds per beat (160 BPM)

# Create instruments
# 1. Drums (Little Ray)
# 2. Bass (Marcus)
# 3. Piano (Diane)
# 4. Tenor Sax (You)

# Add drum instrument
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drum = pretty_midi.Instrument(program=drum_program, is_drum=True)
pm.instruments.append(drum)

# Add bass instrument
bass = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Double Bass'))
pm.instruments.append(bass)

# Add piano
piano = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Acoustic Grand Piano'))
pm.instruments.append(piano)

# Add sax
sax = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Tenor Saxophone'))
pm.instruments.append(sax)

# -------------------
# Bar 1: Little Ray on drums (setup, tension)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Start at time = 0.0

# Kick on 1 and 3
kicks = [0.0, 2 * BEAT_DURATION]
for time in kicks:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drum.notes.append(note)

# Snare on 2 and 4
snares = [1 * BEAT_DURATION, 3 * BEAT_DURATION]
for time in snares:
    note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
    drum.notes.append(note)

# Hihat on every eighth
hihats = [i * BEAT_DURATION for i in range(0, 8)]
for time in hihats:
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
    drum.notes.append(note)

# -------------------
# Bar 2: All instruments in, start melody

# Bass line: walking line, chromatic approaches
# Fm: F, Gb, Ab, Bb, B, Db, Eb
# Bass line: F - Gb - Ab - Bb - B - Db - Eb - F (walk down chromatically)

bass_notes = [
    (0.0, 53),  # F (F3)
    (0.375, 52),  # Gb
    (0.75, 50),  # Ab
    (1.125, 48),  # Bb
    (1.5, 49),  # Bb -> B (chromatic)
    (1.875, 47),  # Db
    (2.25, 46),  # Eb
    (2.625, 53),  # F
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, Bb, Db (Fm7)
# Gm7 = Gb, Bb, Db, F (Gm7)
# Am7 = Ab, C, Eb, G (Am7)
# Bm7 = Bb, Db, F, Ab (Bm7)

# Comp on 2 and 4 of the bar (starting at 1.5s)
comp_times = [1.5, 3.0]
for time in comp_times:
    # Fm7
    note1 = pretty_midi.Note(velocity=90, pitch=53, start=time, end=time + 0.25)
    note2 = pretty_midi.Note(velocity=90, pitch=50, start=time, end=time + 0.25)
    note3 = pretty_midi.Note(velocity=90, pitch=48, start=time, end=time + 0.25)
    note4 = pretty_midi.Note(velocity=90, pitch=47, start=time, end=time + 0.25)
    piano.notes.extend([note1, note2, note3, note4])

# Drums continue: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 starts at 1.5s

# Kick on 1 and 3 (1.5 and 2.25)
kicks = [1.5, 2.25]
for time in kicks:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drum.notes.append(note)

# Snare on 2 and 4 (1.875 and 2.625)
snares = [1.875, 2.625]
for time in snares:
    note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
    drum.notes.append(note)

# Hihat on every eighth
hihats = [1.5 + i * BEAT_DURATION for i in range(0, 8)]
for time in hihats:
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
    drum.notes.append(note)

# -------------------
# Bar 3: Continue bass, piano, drums; sax begins melody

# Tenor sax: sparse, expressive, one short motif
# Start at 3.0s
# Melody: F -> Ab -> Bb -> F (with a slight delay on the last note)

sax_notes = [
    (3.0, 53),  # F
    (3.125, 50),  # Ab
    (3.375, 48),  # Bb
    (3.5, 53),  # F (held)
    (3.75, 53),  # F (ends)
]

for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.1)
    sax.notes.append(note)

# Bass continues walking
bass_notes = [
    (3.0, 51),  # Gb
    (3.375, 50),  # Ab
    (3.75, 48),  # Bb
    (4.125, 49),  # B
    (4.5, 47),  # Db
    (4.875, 46),  # Eb
    (5.25, 53),  # F
    (5.625, 52),  # Gb
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano continues comping on 2 and 4
comp_times = [3.0, 4.5]
for time in comp_times:
    # Gm7
    note1 = pretty_midi.Note(velocity=90, pitch=52, start=time, end=time + 0.25)
    note2 = pretty_midi.Note(velocity=90, pitch=48, start=time, end=time + 0.25)
    note3 = pretty_midi.Note(velocity=90, pitch=47, start=time, end=time + 0.25)
    note4 = pretty_midi.Note(velocity=90, pitch=53, start=time, end=time + 0.25)
    piano.notes.extend([note1, note2, note3, note4])

# Drums continue
# Kick on 1 and 3 (3.0 and 3.75)
kicks = [3.0, 3.75]
for time in kicks:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drum.notes.append(note)

# Snare on 2 and 4 (3.375 and 4.125)
snares = [3.375, 4.125]
for time in snares:
    note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
    drum.notes.append(note)

# Hihat on every eighth
hihats = [3.0 + i * BEAT_DURATION for i in range(0, 8)]
for time in hihats:
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
    drum.notes.append(note)

# -------------------
# Bar 4: Sax resolves the motif, bass continues, piano resolves

# Tenor sax: resolve the motif
# F -> Ab -> Bb -> F (shorter this time, more resolved)
sax_notes = [
    (4.5, 53),  # F
    (4.625, 50),  # Ab
    (4.875, 48),  # Bb
    (5.0, 53),  # F
    (5.125, 53),  # F (ends)
]

for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.1)
    sax.notes.append(note)

# Bass continues walking
bass_notes = [
    (4.5, 49),  # B
    (4.875, 47),  # Db
    (5.25, 46),  # Eb
    (5.625, 53),  # F
    (6.0, 52),  # Gb
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano resolves with a Gm7 chord on 4 (time 4.5)
note1 = pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.75)
note2 = pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.75)
note3 = pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.75)
note4 = pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.75)
piano.notes.extend([note1, note2, note3, note4])

# Drums continue
# Kick on 1 and 3 (4.5 and 5.25)
kicks = [4.5, 5.25]
for time in kicks:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drum.notes.append(note)

# Snare on 2 and 4 (4.875 and 5.625)
snares = [4.875, 5.625]
for time in snares:
    note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
    drum.notes.append(note)

# Hihat on every eighth
hihats = [4.5 + i * BEAT_DURATION for i in range(0, 8)]
for time in hihats:
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
    drum.notes.append(note)

# Save the MIDI file
pm.write("Wayne_intro.mid")
