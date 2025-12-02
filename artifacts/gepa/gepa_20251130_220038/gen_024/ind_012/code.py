
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

# Kicks on 1 and 3, snares on 2 and 4, hihat on every eighth
kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875, 5.625]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125,
               1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125,
               3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125,
               4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.0625)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
# Fm7 = F, Ab, Bb, D
# Walking bass line in Fm
bass_notes = [
    (1.5, 53),  # F
    (1.75, 51),  # Eb (chromatic approach)
    (2.0, 50),  # D
    (2.25, 52),  # F
    (2.5, 51),  # Eb
    (2.75, 50),  # D
    (3.0, 48),  # C (chromatic approach)
    (3.25, 50),  # D
    (3.5, 52),  # F
    (3.75, 51),  # Eb
    (4.0, 50),  # D
    (4.25, 52),  # F
    (4.5, 51),  # Eb
    (4.75, 50),  # D
    (5.0, 48),  # C
    (5.25, 50),  # D
    (5.5, 52),  # F
    (5.75, 51),  # Eb
    (6.0, 50)   # D
]

for t, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, Bb, D
# Comp on beat 2 and 4 (1.75 and 2.25, 3.25 and 3.75, 4.25 and 4.75)
chords = [
    (1.75, [53, 51, 50, 52]),  # Fm7
    (2.25, [53, 51, 50, 52]),
    (3.25, [53, 51, 50, 52]),
    (3.75, [53, 51, 50, 52]),
    (4.25, [53, 51, 50, 52]),
    (4.75, [53, 51, 50, 52])
]

for t, pitches in chords:
    for p in pitches:
        note = pretty_midi.Note(velocity=90, pitch=p, start=t, end=t + 0.25)
        piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (53), Ab (51), Bb (50), F (53)
# Start at bar 2 (1.5s), first note at 1.5s, last note at 2.0s
# Repeat at bar 4 (4.5s), first note at 4.5s, last note at 5.0s

sax_notes = [
    (1.5, 53, 0.25),
    (1.75, 51, 0.25),
    (2.0, 50, 0.25),
    (4.5, 53, 0.25),
    (4.75, 51, 0.25),
    (5.0, 50, 0.25)
]

for t, pitch, duration in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=t, end=t + duration)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
