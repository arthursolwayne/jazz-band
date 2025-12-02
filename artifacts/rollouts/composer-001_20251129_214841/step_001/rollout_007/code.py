
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),   # C
    pretty_midi.Note(velocity=90, pitch=61, start=1.75, end=2.0),   # C#
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25),   # D
    pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.5),   # D#
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=2.75),   # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.75, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),   # F#
    pretty_midi.Note(velocity=90, pitch=68, start=3.25, end=3.5),   # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75),   # G#
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.0),   # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.25),   # A#
    pretty_midi.Note(velocity=90, pitch=72, start=4.25, end=4.5),   # B
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),   # A#
    pretty_midi.Note(velocity=90, pitch=70, start=4.75, end=5.0),   # A
    pretty_midi.Note(velocity=90, pitch=68, start=5.0, end=5.25),   # G
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),   # F#
    pretty_midi.Note(velocity=90, pitch=65, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0),   # E
]
bass.notes.extend(bass_notes)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),   # C7 - B
    pretty_midi.Note(velocity=90, pitch=72, start=1.75, end=2.0),   # C7 - C
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),   # C7 - G
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),   # C7 - Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),   # C7 - B
    pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.5),   # C7 - C
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),   # C7 - G
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),   # C7 - Bb
]
piano.notes.extend(piano_notes)

# Saxophone - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# C - E - Bb - C (Motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),   # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),   # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),   # C
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),   # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),   # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),   # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),   # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
