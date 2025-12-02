
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (34, 1.5, 0.375), (35, 1.875, 0.375), (33, 2.25, 0.375), (32, 2.625, 0.375),
    (34, 3.0, 0.375), (35, 3.375, 0.375), (33, 3.75, 0.375), (32, 4.125, 0.375),
    (34, 4.5, 0.375), (35, 4.875, 0.375), (33, 5.25, 0.375), (32, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    (53, 1.875, 0.375), (60, 1.875, 0.375), (64, 1.875, 0.375), (65, 1.875, 0.375),
    # Bar 3: Bbm7 (Bb, Db, F, Ab)
    (57, 3.375, 0.375), (62, 3.375, 0.375), (59, 3.375, 0.375), (60, 3.375, 0.375),
    # Bar 4: Eb7 (Eb, G, Bb, D)
    (62, 4.875, 0.375), (67, 4.875, 0.375), (60, 4.875, 0.375), (65, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: full bar with kick, snare, hihat
for bar_start in [1.5, 3.0, 4.5]:
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5))
    # Hihat on every eighth
    for i in range(8):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + i*0.375, end=bar_start + i*0.375 + 0.1875))

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Fm7 -> Bb7 -> Eb7 -> Fm7
motif = [
    (53, 1.5, 0.375), # F
    (57, 1.875, 0.375), # Bb
    (62, 2.25, 0.375), # Eb
    (53, 2.625, 0.375), # F
    (53, 3.0, 0.375), # F
    (57, 3.375, 0.375), # Bb
    (62, 3.75, 0.375), # Eb
    (53, 4.125, 0.375)  # F
]
for note, start, duration in motif:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
