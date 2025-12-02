
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # A
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # B
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # F
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # F
]
piano.notes.extend(piano_notes)

# Sax solo - short motif, make it sing
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.6875),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0625), # F
    pretty_midi.Note(velocity=100, pitch=65, start=2.0625, end=2.25),  # G
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.1875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.1875, end=3.375), # B
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5625), # A
    pretty_midi.Note(velocity=100, pitch=66, start=3.5625, end=3.75),  # G
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.6875, end=4.875), # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0625), # A
    pretty_midi.Note(velocity=100, pitch=69, start=5.0625, end=5.25),  # B
    # Resolution
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.4375), # A
    pretty_midi.Note(velocity=100, pitch=65, start=5.4375, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.8125), # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.8125, end=6.0),  # E
]
sax.notes.extend(sax_notes)

# Drums: continue pattern for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    midi_note = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    drums.notes.append(midi_note)
    midi_note = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    drums.notes.append(midi_note)
    # Snare on 2 and 4
    midi_note = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    drums.notes.append(midi_note)
    midi_note = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    drums.notes.append(midi_note)
    # Hihat on every eighth
    for i in range(8):
        midi_note = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)
        drums.notes.append(midi_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
