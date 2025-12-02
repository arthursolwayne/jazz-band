
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125, 1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125, 3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125, 4.5, 4.6875, 4.875, 5.0625, 5.25]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=90, pitch=42, start=t, end=t + 0.0625)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm, chromatic approaches
bass_notes = [
    (1.5, 45), # F
    (1.875, 46), # Gb
    (2.25, 43), # D
    (2.625, 44), # Eb
    (3.0, 45), # F
    (3.375, 46), # Gb
    (3.75, 43), # D
    (4.125, 44), # Eb
    (4.5, 45), # F
    (4.875, 46), # Gb
    (5.25, 43), # D
    (5.625, 44)  # Eb
]

for t, pitch in bass_notes:
    note = pretty_midi.Note(velocity=95, pitch=pitch, start=t, end=t + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comping on 2 and 4
# Fm7 on beat 2 of bar 2, Bb7 on beat 4 of bar 2
# Am7 on beat 2 of bar 3, D7 on beat 4 of bar 3
# Fm7 on beat 2 of bar 4, Gm7 on beat 4 of bar 4

def add_chord(start, chord):
    for note in chord:
        pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.25)

# Fm7 = F, Ab, C, Eb
# Bb7 = Bb, D, F, Ab
# Am7 = A, C, E, G
# D7 = D, F#, A, C
# Gm7 = G, Bb, D, F

chords = [
    (2.25, [53, 55, 57, 59]), # Bb7
    (2.625, [53, 55, 57, 59]),
    (3.375, [57, 59, 62, 64]), # Am7
    (3.75, [57, 59, 62, 64]),
    (4.5, [53, 55, 57, 59]), # Bb7
    (4.875, [67, 69, 71, 72]) # Gm7
]

for t, notes in chords:
    for note in notes:
        piano_note = pretty_midi.Note(velocity=100, pitch=note, start=t, end=t + 0.25)
        piano.notes.append(piano_note)

# Sax: Main motif
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Motif: F -> Ab -> Bb -> C, with a short rest on the last note

sax_notes = [
    (1.5, 53), # F
    (1.6875, 55), # Ab
    (1.875, 57), # Bb
    (2.0625, 58), # C
    (2.125, 53), # F (return)
    (2.3125, 55), # Ab
    (2.5, 57), # Bb
    (2.6875, 58), # C
    (2.75, 53), # F
    (2.9375, 55), # Ab
    (3.125, 57), # Bb
    (3.3125, 58), # C
    (3.375, 53), # F
    (3.5625, 55), # Ab
    (3.75, 57), # Bb
    (3.9375, 58), # C
]

for t, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=t, end=t + 0.125)
    sax.notes.append(note)

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
