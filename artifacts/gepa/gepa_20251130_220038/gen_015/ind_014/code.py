
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
drum_notes = [
    (36, 0.0, 1.0),     # Kick on 1
    (42, 0.25, 0.25),   # Hi-hat on 2
    (38, 0.5, 1.0),     # Snare on 3
    (42, 0.75, 0.25),   # Hi-hat on 4
    (42, 1.0, 0.5)      # Hi-hat on 4
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - Walking line in Fm, chromatic approaches
bass_notes = [
    (43, 1.5, 0.375),   # F
    (42, 1.875, 0.375), # Eb
    (44, 2.25, 0.375),  # F
    (45, 2.625, 0.375), # Gb
    (47, 2.625, 0.375), # Ab
    (46, 3.0, 0.375),   # Gb
    (45, 3.375, 0.375), # F
    (44, 3.75, 0.375),  # Eb
    (43, 4.125, 0.375), # F
    (42, 4.5, 0.375),   # Eb
    (44, 4.875, 0.375), # F
    (45, 5.25, 0.375)   # Gb
]
for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + dur))

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    (45, 1.5, 0.375),   # F7 (F, A, C, Eb) - C
    (50, 1.5, 0.375),   # F7 - A
    (53, 1.5, 0.375),   # F7 - Eb
    (46, 1.875, 0.375), # Bb7 (Bb, D, F, Ab) - D
    (51, 1.875, 0.375), # Bb7 - F
    (53, 1.875, 0.375), # Bb7 - Ab
    (45, 2.25, 0.375),  # F7 - F
    (50, 2.25, 0.375),  # F7 - A
    (53, 2.25, 0.375),  # F7 - Eb
    (46, 2.625, 0.375), # Bb7 - D
    (51, 2.625, 0.375), # Bb7 - F
    (53, 2.625, 0.375), # Bb7 - Ab
    (45, 3.0, 0.375),   # F7 - F
    (50, 3.0, 0.375),   # F7 - A
    (53, 3.0, 0.375),   # F7 - Eb
    (46, 3.375, 0.375), # Bb7 - D
    (51, 3.375, 0.375), # Bb7 - F
    (53, 3.375, 0.375), # Bb7 - Ab
    (45, 3.75, 0.375),  # F7 - F
    (50, 3.75, 0.375),  # F7 - A
    (53, 3.75, 0.375),  # F7 - Eb
    (46, 4.125, 0.375), # Bb7 - D
    (51, 4.125, 0.375), # Bb7 - F
    (53, 4.125, 0.375), # Bb7 - Ab
    (45, 4.5, 0.375),   # F7 - F
    (50, 4.5, 0.375),   # F7 - A
    (53, 4.5, 0.375),   # F7 - Eb
    (46, 4.875, 0.375), # Bb7 - D
    (51, 4.875, 0.375), # Bb7 - F
    (53, 4.875, 0.375)  # Bb7 - Ab
]
for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Drums (Little Ray) - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick1 = (36, bar_start, 1.0)
    snare2 = (38, bar_start + 0.5, 1.0)
    hihat = [(42, bar_start + i * 0.25, 0.25) for i in range(0, 4)]
    kick3 = (36, bar_start + 1.5, 1.0)
    snare4 = (38, bar_start + 2.0, 1.0)
    for note, start, dur in [kick1, snare2, kick3, snare4] + hihat:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Saxophone (Dante) - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (43), Ab (45), Gb (44), F (43)
sax_notes = [
    (43, 1.5, 0.375),   # F
    (45, 1.875, 0.375), # Ab
    (44, 2.25, 0.375),  # Gb
    (43, 2.625, 0.375), # F
    (43, 3.5, 0.25),    # F (pickup)
    (45, 3.75, 0.375),  # Ab
    (44, 4.125, 0.375), # Gb
    (43, 4.5, 0.375)    # F
]
for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + dur))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
