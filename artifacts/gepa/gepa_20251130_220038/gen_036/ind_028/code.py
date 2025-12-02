
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus: Walking line, chromatic approaches, never the same note twice.
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=37, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=80, pitch=34, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=80, pitch=35, start=2.625, end=3.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=32, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=33, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=80, pitch=30, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=80, pitch=31, start=4.125, end=4.5),  # F#
    pretty_midi.Note(velocity=80, pitch=28, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=29, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=80, pitch=26, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=80, pitch=27, start=5.625, end=6.0),  # B
]
bass.notes.extend(bass_notes)

# Piano - Diane: 7th chords, comp on 2 and 4.
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # F7 - F
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # F7 - A
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F7 - C
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.875),  # F7 - E
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375),  # F7 - F
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # F7 - A
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # F7 - C
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # F7 - E
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),  # F7 - F
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # F7 - A
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F7 - C
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.875),  # F7 - E
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    # Snare on 3
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
drums.notes.extend([n for n in drum_notes if n not in drums.notes])

# Sax - Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start the motif (F, Ab, Bb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=110, pitch=50, start=2.25, end=2.625), # Bb
    # Bar 3: Silence (leave it hanging)
    # Bar 4: Return and finish the motif (F, Ab, Bb, D)
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=110, pitch=50, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=110, pitch=55, start=5.625, end=6.0),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_intro.mid')
