
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

# Bar 2-4 (1.5 - 6.0s)
# Bass line (Marcus) - walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5 - 3.0)
    (1.5, 62, 100), (1.75, 64, 100), (2.0, 65, 100), (2.25, 67, 100),
    # Bar 3 (3.0 - 4.5)
    (3.0, 69, 100), (3.25, 71, 100), (3.5, 72, 100), (3.75, 74, 100),
    # Bar 4 (4.5 - 6.0)
    (4.5, 76, 100), (4.75, 78, 100), (5.0, 79, 100), (5.25, 81, 100)
]
for start, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0)
    (1.75, 67, 100), (2.0, 72, 100), (2.25, 74, 100), (2.5, 79, 100),
    # Bar 3 (3.0 - 4.5)
    (3.25, 67, 100), (3.5, 72, 100), (3.75, 74, 100), (4.0, 79, 100),
    # Bar 4 (4.5 - 6.0)
    (4.75, 67, 100), (5.0, 72, 100), (5.25, 74, 100), (5.5, 79, 100)
]
for start, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    piano.notes.append(note)

# Sax (Dante) - short motif, starts on beat 2 of bar 2, ends on beat 3 of bar 4
# Motif: D (62) -> F# (66) -> B (71) -> D (62) -> G (67) -> B (71)
sax_notes = [
    (1.75, 62, 110), (2.0, 66, 110), (2.25, 71, 110),
    (3.0, 62, 110), (3.25, 67, 110), (3.5, 71, 110),
    (4.5, 62, 110), (4.75, 66, 110), (5.0, 71, 110)
]
for start, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
