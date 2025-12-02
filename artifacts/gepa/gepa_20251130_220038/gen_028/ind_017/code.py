
import pretty_midi

# Create a new MIDI file at 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 1, 2, 3]:  # 0 = 0s, 1 = 0.375s, 2 = 0.75s, 3 = 1.125s
    # Hihat on every eighth
    note = pretty_midi.Note(velocity=100, pitch=hihat, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)

    # Kick on 1 and 3 (beat 0 and 2)
    if beat == 0 or beat == 2:
        note = pretty_midi.Note(velocity=110, pitch=kick, start=beat * 0.375, end=(beat + 1) * 0.375)
        drums.notes.append(note)

    # Snare on 2 and 4 (beat 1 and 3)
    if beat == 1 or beat == 3:
        note = pretty_midi.Note(velocity=105, pitch=snare, start=beat * 0.375, end=(beat + 1) * 0.375)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeating notes
# Fm = F, Ab, Bb, C, Eb, G, Ab
# Walking bass in Fm (key of F minor)
# Bar 2: F, Gb, Ab, A
# Bar 3: Bb, C, Db, D
# Bar 4: Eb, F, G, Ab

bass_notes = [
    (1.5, 75),  # F (75)
    (1.875, 71),  # Gb (71)
    (2.25, 77),  # Ab (77)
    (2.625, 79),  # A (79)
    (3.0, 71),  # Bb (71)
    (3.375, 72),  # C (72)
    (3.75, 70),  # Db (70)
    (4.125, 72),  # D (72)
    (4.5, 69),  # Eb (69)
    (4.875, 75),  # F (75)
    (5.25, 77),  # G (77)
    (5.625, 77),  # Ab (77)
]

for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: Fm7 (F, Ab, Bb, C)
# Bar 3: Bbm7 (Bb, Db, Eb, F)
# Bar 4: Ebm7 (Eb, Gb, Ab, Bb)

# Comp on 2 and 4 (beat 1 and 3 in each bar)
# Bar 2: 1.875 and 2.625
# Bar 3: 3.375 and 4.125
# Bar 4: 4.875 and 5.625

piano_notes = [
    (1.875, 75),  # F
    (1.875, 77),  # Ab
    (1.875, 71),  # Bb
    (1.875, 72),  # C

    (2.625, 71),  # Bb
    (2.625, 70),  # Db
    (2.625, 69),  # Eb
    (2.625, 75),  # F

    (3.375, 69),  # Eb
    (3.375, 71),  # Gb
    (3.375, 77),  # Ab
    (3.375, 71),  # Bb

    (4.125, 69),  # Eb
    (4.125, 71),  # Gb
    (4.125, 77),  # Ab
    (4.125, 71),  # Bb

    (4.875, 75),  # F
    (4.875, 77),  # Ab
    (4.875, 71),  # Bb
    (4.875, 72),  # C

    (5.625, 69),  # Eb
    (5.625, 71),  # Gb
    (5.625, 77),  # Ab
    (5.625, 71),  # Bb
]

for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375)
    piano.notes.append(note)

# Sax: Your motif. One short melody. Start it, leave it hanging. Come back and finish it.

# Melody in F minor: F, Ab, Bb, C (Fm7), then a harmonic twist
# Bar 2: F (75), Ab (77), Bb (71), C (72)
# Bar 3: F (75), Ab (77), Bb (71), B (73) — a bluesy, unexpected note
# Bar 4: F (75), Ab (77), C (72), D (74) — resolution and a touch of tension

sax_notes = [
    (1.5, 75),  # F
    (1.875, 77),  # Ab
    (2.25, 71),  # Bb
    (2.625, 72),  # C

    (3.0, 75),  # F
    (3.375, 77),  # Ab
    (3.75, 71),  # Bb
    (4.125, 73),  # B — tension

    (4.5, 75),  # F
    (4.875, 77),  # Ab
    (5.25, 72),  # C
    (5.625, 74),  # D — tension and resolution
]

for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.375)
    sax.notes.append(note)

# Add all instruments to the MIDI file
midi.instruments.append(sax)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)

# Save the MIDI file
midi.write("dante_russo_intro.mid")
