
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
kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125,
               1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125,
               3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125,
               4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375]

drum_notes = []
for t in kick_times:
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.125))
for t in snare_times:
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.125))
for t in hihat_times:
    drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=t, end=t + 0.125))

drums.notes.extend(drum_notes)

# Bar 2: All instruments enter

# Sax - D (D4), F# (F#4), A (A4), B (B4) - motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # A4
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.5),  # B4
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.5),  # F#4
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),  # A4
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.0),  # B4
]

sax.notes.extend(sax_notes)

# Bass - Walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=90, pitch=44, start=1.75, end=2.0),  # Eb3
    pretty_midi.Note(velocity=90, pitch=45, start=2.0, end=2.25),  # E3
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.5),  # G3
    pretty_midi.Note(velocity=90, pitch=48, start=2.5, end=2.75),  # G#3
    pretty_midi.Note(velocity=90, pitch=50, start=2.75, end=3.0),  # A3
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.25),  # B3
    pretty_midi.Note(velocity=90, pitch=53, start=3.25, end=3.5),  # C4
    pretty_midi.Note(velocity=90, pitch=55, start=3.5, end=3.75),  # D4
    pretty_midi.Note(velocity=90, pitch=56, start=3.75, end=4.0),  # Eb4
    pretty_midi.Note(velocity=90, pitch=57, start=4.0, end=4.25),  # E4
    pretty_midi.Note(velocity=90, pitch=59, start=4.25, end=4.5),  # G4
]

bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4, Dmi7, G7, A7, Dmi7
piano_notes = [
    # Bar 2 - 2 and 4
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),  # B4

    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # B4
]

piano_notes += [
    # Bar 3 - 2 and 4
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),  # B4

    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),  # B4
]

piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
