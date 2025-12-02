
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - walking line, chromatic approaches, never the same note twice
bass_notes = []
# Fm7 chord: F, Ab, C, Eb
# Walking bass line in Fm7
bass_line = [64, 63, 60, 62, 64, 63, 60, 62, 64, 63, 60, 62, 64, 63, 60, 62]
for i, note in enumerate(bass_line):
    start = 1.5 + i * 0.375
    end = start + 0.375
    bass_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane - 7th chords, comp on 2 and 4
piano_notes = []
# Fm7: F, Ab, C, Eb
# Bb7: Bb, D, F, Ab
# Cm7: C, Eb, G, Bb
# Eb7: Eb, G, Bb, D
# Comp on 2 and 4
# Bar 2: Fm7
for note in [64, 67, 72, 69]:
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=1.5, end=1.875))
# Bar 3: Bb7
for note in [67, 71, 64, 67]:
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=2.625, end=2.875))
# Bar 4: Cm7
for note in [72, 69, 76, 71]:
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=3.75, end=4.125))
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Motif: F, Ab, C, Eb (Fm7 arpeggio)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),
    # Leave it hanging
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),
    # Come back and finish it
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),
]
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
