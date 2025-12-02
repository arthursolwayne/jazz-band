
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
    # Bar 1
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875), (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (36, 1.125, 0.375),
    (38, 1.5, 0.375), (42, 1.5, 0.1875),
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi_note(note, start, duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line - Marcus
bass_notes = [
    (62, 1.5, 0.375), (64, 1.875, 0.375), (63, 2.25, 0.375), (61, 2.625, 0.375),
    (62, 3.0, 0.375), (64, 3.375, 0.375), (63, 3.75, 0.375), (61, 4.125, 0.375),
    (62, 4.5, 0.375), (64, 4.875, 0.375), (63, 5.25, 0.375), (61, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi_note(note, start, duration))

# Piano - Diane - 7th chords, comp on 2 and 4
piano_notes = [
    (62, 1.875, 0.375), (66, 1.875, 0.375), (67, 1.875, 0.375), (69, 1.875, 0.375),
    (62, 3.0, 0.375), (66, 3.0, 0.375), (67, 3.0, 0.375), (69, 3.0, 0.375),
    (62, 4.5, 0.375), (66, 4.5, 0.375), (67, 4.5, 0.375), (69, 4.5, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi_note(note, start, duration))

# Sax - Dante
sax_notes = [
    (62, 1.5, 0.375),
    (64, 1.875, 0.375),
    (64, 2.25, 0.375),
    (62, 2.625, 0.375),
    (60, 3.0, 0.375),
    (62, 3.375, 0.375),
    (64, 3.75, 0.375),
    (62, 4.125, 0.375),
    (60, 4.5, 0.375),
    (62, 4.875, 0.375),
    (64, 5.25, 0.375),
    (62, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi_note(note, start, duration))

# Drums for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi_note(36, start, 0.375)
    kick3 = pretty_midi_note(36, start + 0.75, 0.375)
    # Snare on 2 and 4
    snare2 = pretty_midi_note(38, start + 0.375, 0.375)
    snare4 = pretty_midi_note(38, start + 1.125, 0.375)
    # Hi-hat on every eighth
    hihat = [pretty_midi_note(42, start + i * 0.1875, 0.1875) for i in range(8)]
    for note in [kick1, kick3, snare2, snare4] + hihat:
        drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
