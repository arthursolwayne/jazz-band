
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42
# Notes for drums
drum_notes = []

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    time = i * 0.375
    if i % 2 == 0:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375))
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375))
    else:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.375))
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: chromatic approach, walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=63, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # C#
    pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0),  # D
]

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # B
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # C#
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625), # D
    # Bar 2, beat 4: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # B
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # C#
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375), # D
    # Bar 3, beat 2: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5), # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5), # B
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5), # C#
    pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.5), # D
    # Bar 3, beat 4: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # B
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25), # C#
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25), # D
    # Bar 4, beat 2: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0), # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0), # B
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0), # C#
    pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0), # D
]

# Saxophone: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, E, F, G, Ab, A, Bb
# Motif: D, Eb, E, rest, then G, Ab, A, Bb
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625), # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75), # Eb
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=1.875), # E
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.125), # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.125, end=2.25), # Ab
    pretty_midi.Note(velocity=110, pitch=70, start=2.25, end=2.375), # A
    pretty_midi.Note(velocity=110, pitch=71, start=2.375, end=2.5),  # Bb
]

# Add notes to instruments
drums.notes.extend(drum_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('intro.mid')
