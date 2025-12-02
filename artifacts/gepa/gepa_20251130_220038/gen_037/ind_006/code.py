
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (36, 0.0), (38, 0.75), (42, 0.0), (42, 0.375), (42, 0.75), (42, 1.125),
    (36, 1.5), (38, 2.25), (42, 1.5), (42, 1.875), (42, 2.25), (42, 2.625),
]

for note_number, time in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus
bass_notes = [
    # Bar 2
    (37, 1.5), (36, 1.75), (38, 2.0), (39, 2.25),
    # Bar 3
    (40, 2.5), (39, 2.75), (38, 3.0), (37, 3.25),
    # Bar 4
    (38, 3.5), (39, 3.75), (40, 4.0), (41, 4.25),
]
for note_number, time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_number, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: Diane - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.75), (64, 1.75), (67, 1.75), (69, 1.75),
    # Bar 3
    (62, 2.75), (64, 2.75), (67, 2.75), (69, 2.75),
    # Bar 4
    (62, 3.75), (64, 3.75), (67, 3.75), (69, 3.75),
]
for note_number, time in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: Dante - Melody
# Start with a whisper, build to a cry
# Bar 2: start of melody
sax_notes = [
    # Bar 2
    (62, 1.5), (65, 1.875), (67, 2.25),
    # Bar 3
    (69, 2.5), (67, 2.875), (65, 3.25),
    # Bar 4
    (62, 3.5), (64, 3.875), (67, 4.25),
]
for note_number, time in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.375)
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("cellar_intro.mid")
