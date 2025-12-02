
import pretty_midi

# Initialize the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1 (0.0 - 1.5s): Little Ray on drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    bar_start = bar * 1.5
    # Kick on 1 and 3 (beat 0 and 2)
    for kick_beat in [0, 2]:
        kick_time = bar_start + kick_beat * 0.375
        kick_note = pretty_midi.Note(velocity=100, pitch=KICK, start=kick_time, end=kick_time + 0.1)
        drums.notes.append(kick_note)
    # Snare on 2 and 4 (beat 1 and 3)
    for snare_beat in [1, 3]:
        snare_time = bar_start + snare_beat * 0.375
        snare_note = pretty_midi.Note(velocity=100, pitch=SNARE, start=snare_time, end=snare_time + 0.1)
        drums.notes.append(snare_note)
    # Hi-hat on every eighth
    for hihat_beat in range(8):
        hihat_time = bar_start + hihat_beat * 0.125
        hihat_note = pretty_midi.Note(velocity=90, pitch=HIHAT, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat_note)

# Bar 2 (1.5 - 3.0s): Full quartet - sax melody
bar_start = 1.5
# Sax melody: F7 -> Ab7 -> Bb7 -> F7 (motif based on F7 chord)
# F7 (F, A, C, Eb)
# Ab7 (Ab, C, Eb, Gb)
# Bb7 (Bb, D, F, Ab)
# F7 again

# Motif: F (beat 0), Ab (beat 1), Bb (beat 2), F (beat 3)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=bar_start, end=bar_start + 0.375),  # F (71)
    pretty_midi.Note(velocity=100, pitch=68, start=bar_start + 0.375, end=bar_start + 0.75),  # Ab (68)
    pretty_midi.Note(velocity=100, pitch=70, start=bar_start + 0.75, end=bar_start + 1.125),  # Bb (70)
    pretty_midi.Note(velocity=100, pitch=71, start=bar_start + 1.125, end=bar_start + 1.5),  # F (71)
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F (F, Gb, G, A, Bb, B, C, Db)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=bar_start, end=bar_start + 0.375),  # F (65)
    pretty_midi.Note(velocity=90, pitch=66, start=bar_start + 0.375, end=bar_start + 0.75),  # Gb (66)
    pretty_midi.Note(velocity=90, pitch=67, start=bar_start + 0.75, end=bar_start + 1.125),  # G (67)
    pretty_midi.Note(velocity=90, pitch=69, start=bar_start + 1.125, end=bar_start + 1.5),  # A (69)
]
bass.notes.extend(bass_notes)

# Piano: Comping on 2 and 4 (7th chords)
# F7 on beat 2, G7 on beat 4
piano_notes = [
    # F7 (F, A, C, Eb) on beat 2 (time = 1.5 + 0.75 = 2.25s)
    pretty_midi.Note(velocity=90, pitch=71, start=bar_start + 0.75, end=bar_start + 1.125),  # F (71)
    pretty_midi.Note(velocity=90, pitch=74, start=bar_start + 0.75, end=bar_start + 1.125),  # A (74)
    pretty_midi.Note(velocity=90, pitch=76, start=bar_start + 0.75, end=bar_start + 1.125),  # C (76)
    pretty_midi.Note(velocity=90, pitch=73, start=bar_start + 0.75, end=bar_start + 1.125),  # Eb (73)
    
    # G7 (G, B, D, F) on beat 4 (time = 1.5 + 1.5 = 3.0s)
    pretty_midi.Note(velocity=90, pitch=72, start=bar_start + 1.5, end=bar_start + 1.875),  # G (72)
    pretty_midi.Note(velocity=90, pitch=76, start=bar_start + 1.5, end=bar_start + 1.875),  # B (76)
    pretty_midi.Note(velocity=90, pitch=78, start=bar_start + 1.5, end=bar_start + 1.875),  # D (78)
    pretty_midi.Note(velocity=90, pitch=76, start=bar_start + 1.5, end=bar_start + 1.875),  # F (76)
]
piano.notes.extend(piano_notes)

# Bar 3 (3.0 - 4.5s): Full quartet
bar_start = 3.0
# Sax: Repeat the motif, but start on Bb (70) and resolve to F (71)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=bar_start, end=bar_start + 0.375),  # Bb (70)
    pretty_midi.Note(velocity=100, pitch=71, start=bar_start + 0.375, end=bar_start + 0.75),  # F (71)
    pretty_midi.Note(velocity=100, pitch=73, start=bar_start + 0.75, end=bar_start + 1.125),  # Eb (73)
    pretty_midi.Note(velocity=100, pitch=71, start=bar_start + 1.125, end=bar_start + 1.5),  # F (71)
]
sax.notes.extend(sax_notes)

# Bass: Walking line (F, Gb, G, A, Bb, B, C, Db)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=bar_start, end=bar_start + 0.375),  # F (65)
    pretty_midi.Note(velocity=90, pitch=66, start=bar_start + 0.375, end=bar_start + 0.75),  # Gb (66)
    pretty_midi.Note(velocity=90, pitch=67, start=bar_start + 0.75, end=bar_start + 1.125),  # G (67)
    pretty_midi.Note(velocity=90, pitch=69, start=bar_start + 1.125, end=bar_start + 1.5),  # A (69)
]
bass.notes.extend(bass_notes)

# Piano: Comping on 2 and 4 (Eb7 on beat 2, F7 on beat 4)
piano_notes = [
    # Eb7 (Eb, G, Bb, Db) on beat 2 (time = 3.0 + 0.75 = 3.75s)
    pretty_midi.Note(velocity=90, pitch=73, start=bar_start + 0.75, end=bar_start + 1.125),  # Eb (73)
    pretty_midi.Note(velocity=90, pitch=76, start=bar_start + 0.75, end=bar_start + 1.125),  # G (76)
    pretty_midi.Note(velocity=90, pitch=71, start=bar_start + 0.75, end=bar_start + 1.125),  # Bb (71)
    pretty_midi.Note(velocity=90, pitch=69, start=bar_start + 0.75, end=bar_start + 1.125),  # Db (69)
    
    # F7 (F, A, C, Eb) on beat 4 (time = 3.0 + 1.5 = 4.5s)
    pretty_midi.Note(velocity=90, pitch=71, start=bar_start + 1.5, end=bar_start + 1.875),  # F (71)
    pretty_midi.Note(velocity=90, pitch=74, start=bar_start + 1.5, end=bar_start + 1.875),  # A (74)
    pretty_midi.Note(velocity=90, pitch=76, start=bar_start + 1.5, end=bar_start + 1.875),  # C (76)
    pretty_midi.Note(velocity=90, pitch=73, start=bar_start + 1.5, end=bar_start + 1.875),  # Eb (73)
]
piano.notes.extend(piano_notes)

# Bar 4 (4.5 - 6.0s): Full quartet
bar_start = 4.5
# Sax: Repeat the motif but resolve to Bb (70) and hold it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=bar_start, end=bar_start + 0.375),  # Bb (70)
    pretty_midi.Note(velocity=100, pitch=73, start=bar_start + 0.375, end=bar_start + 0.75),  # Eb (73)
    pretty_midi.Note(velocity=100, pitch=73, start=bar_start + 0.75, end=bar_start + 1.125),  # Eb (73)
    pretty_midi.Note(velocity=100, pitch=70, start=bar_start + 1.125, end=bar_start + 1.5),  # Bb (70)
]
sax.notes.extend(sax_notes)

# Bass: Walking line (F, Gb, G, A, Bb, B, C, Db)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=bar_start, end=bar_start + 0.375),  # F (65)
    pretty_midi.Note(velocity=90, pitch=66, start=bar_start + 0.375, end=bar_start + 0.75),  # Gb (66)
    pretty_midi.Note(velocity=90, pitch=67, start=bar_start + 0.75, end=bar_start + 1.125),  # G (67)
    pretty_midi.Note(velocity=90, pitch=69, start=bar_start + 1.125, end=bar_start + 1.5),  # A (69)
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 (G7 on beat 2, Bb7 on beat 4)
piano_notes = [
    # G7 (G, B, D, F) on beat 2 (time = 4.5 + 0.75 = 5.25s)
    pretty_midi.Note(velocity=90, pitch=72, start=bar_start + 0.75, end=bar_start + 1.125),  # G (72)
    pretty_midi.Note(velocity=90, pitch=76, start=bar_start + 0.75, end=bar_start + 1.125),  # B (76)
    pretty_midi.Note(velocity=90, pitch=78, start=bar_start + 0.75, end=bar_start + 1.125),  # D (78)
    pretty_midi.Note(velocity=90, pitch=76, start=bar_start + 0.75, end=bar_start + 1.125),  # F (76)
    
    # Bb7 (Bb, D, F, Ab) on beat 4 (time = 4.5 + 1.5 = 6.0s)
    pretty_midi.Note(velocity=90, pitch=71, start=bar_start + 1.5, end=bar_start + 1.875),  # Bb (71)
    pretty_midi.Note(velocity=90, pitch=78, start=bar_start + 1.5, end=bar_start + 1.875),  # D (78)
    pretty_midi.Note(velocity=90, pitch=76, start=bar_start + 1.5, end=bar_start + 1.875),  # F (76)
    pretty_midi.Note(velocity=90, pitch=70, start=bar_start + 1.5, end=bar_start + 1.875),  # Ab (70)
]
piano.notes.extend(piano_notes)

# Add drums for Bar 3 and 4
for bar in range(2, 4):
    bar_start = bar * 1.5
    # Kick on 1 and 3 (beat 0 and 2)
    for kick_beat in [0, 2]:
        kick_time = bar_start + kick_beat * 0.375
        kick_note = pretty_midi.Note(velocity=100, pitch=KICK, start=kick_time, end=kick_time + 0.1)
        drums.notes.append(kick_note)
    # Snare on 2 and 4 (beat 1 and 3)
    for snare_beat in [1, 3]:
        snare_time = bar_start + snare_beat * 0.375
        snare_note = pretty_midi.Note(velocity=100, pitch=SNARE, start=snare_time, end=snare_time + 0.1)
        drums.notes.append(snare_note)
    # Hi-hat on every eighth
    for hihat_beat in range(8):
        hihat_time = bar_start + hihat_beat * 0.125
        hihat_note = pretty_midi.Note(velocity=90, pitch=HIHAT, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat_note)

# Add instruments to MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write out to file
midi.write("dante_intro.mid")
