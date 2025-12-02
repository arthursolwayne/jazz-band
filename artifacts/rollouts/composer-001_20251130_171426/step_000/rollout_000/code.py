
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([kick, snare, hihat])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - walking bass line in D (D, F#, A, B, D, F#, A, B)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),   # B
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),   # B
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),   # B
]
bass.notes.extend(bass_notes)

# Diane - 7th chords on 2 and 4
# D7 on beat 2, G7 on beat 4
# Bar 2: D7 on 2, G7 on 4
d7 = [62, 67, 69, 71]  # D, F#, A, B
g7 = [67, 72, 74, 76]  # G, B, D, F#

# Bar 2 (1.5 - 3.0s)
diane_notes = []
for note in d7:
    diane_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=1.875, end=2.25))
for note in g7:
    diane_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=2.625, end=3.0))

# Bar 3 (3.0 - 4.5s)
for note in d7:
    diane_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=3.875, end=4.25))
for note in g7:
    diane_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=4.625, end=5.0))

# Bar 4 (4.5 - 6.0s)
for note in d7:
    diane_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=5.875, end=6.25))
piano.notes.extend(diane_notes)

# Little Ray - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 1.5)
    drums.notes.extend([kick, snare, hihat])

# Dante - saxophone motif
# D (62) -> F# (67) -> A (69) -> B (71), then D (62) again on beat 3
# Start on beat 2 of bar 2 (1.875s), end on beat 3 (2.25s), then resolve on beat 3 of bar 4 (5.625s)

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=2.75),  # F#
    pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=2.875),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=2.875, end=3.0),   # B
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),   # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
