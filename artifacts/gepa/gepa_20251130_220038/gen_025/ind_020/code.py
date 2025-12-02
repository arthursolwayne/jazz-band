
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
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 1.125), (38, 1.5), (42, 1.5)
]
for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    (62, 1.5), (63, 1.875), (61, 2.25), (60, 2.625),
    (62, 3.0), (63, 3.375), (61, 3.75), (60, 4.125),
    (62, 4.5), (63, 4.875), (61, 5.25), (60, 5.625)
]
for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125)
    bass.notes.append(bass_note)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5-3.0s)
    (60, 1.875), (64, 1.875), (67, 1.875), (71, 1.875),
    (60, 3.0), (64, 3.0), (67, 3.0), (71, 3.0),
    # Bar 3 (3.0-4.5s)
    (62, 4.125), (66, 4.125), (69, 4.125), (73, 4.125),
    (62, 4.5), (66, 4.5), (69, 4.5), (73, 4.5),
    # Bar 4 (4.5-6.0s)
    (64, 5.625), (68, 5.625), (71, 5.625), (75, 5.625),
    (64, 6.0), (68, 6.0), (71, 6.0), (75, 6.0)
]
for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(piano_note)

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    kick_time = start + 0.0
    snare_time = start + 0.375
    hihat_time = start + 0.125
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.125)
    snare_note = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.125)
    hihat_notes = [
        (hihat_time + i * 0.25, 42) for i in range(4)
    ]
    for time, pitch in hihat_notes:
        hihat_note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
        drums.notes.append(hihat_note)
    drums.notes.append(kick_note)
    drums.notes.append(snare_note)

# Sax (Dante) - motif: Dm7 -> E♭ -> Dm7 -> F -> Dm7
sax_notes = [
    # Bar 2 (1.5-3.0s)
    (62, 1.5), (62, 1.5 + 0.125),
    (60, 1.875), (60, 1.875 + 0.125),
    (62, 2.25), (62, 2.25 + 0.125),
    (65, 2.625), (65, 2.625 + 0.125),
    # Bar 3 (3.0-4.5s)
    (62, 3.0), (62, 3.0 + 0.125),
    (60, 3.375), (60, 3.375 + 0.125),
    (62, 3.75), (62, 3.75 + 0.125),
    (64, 4.125), (64, 4.125 + 0.125),
    # Bar 4 (4.5-6.0s)
    (62, 4.5), (62, 4.5 + 0.125),
    (60, 4.875), (60, 4.875 + 0.125),
    (62, 5.25), (62, 5.25 + 0.125),
    (62, 5.625), (62, 5.625 + 0.125)
]
for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
